import os
import datetime
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_sslify import SSLify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from math import ceil
if os.path.exists("env.py"):
    import env


# ======== CONFIGURATION ======== #


app = Flask(__name__)
sslify = SSLify(app)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ======== INDEX PAGE ======== #


# index cocktails
@app.route('/')
def index():

    """
        Display cocktails in index page.

        Fetch all cocktail data from MongoDB cocktails collection.

        Returns:
        template: index.html.

    """

    cocktails = list(
                mongo.db.cocktails.find({"created_by": "admin"}).limit(6))
    return render_template("index.html", cocktails=cocktails)


# Subscribe box
@ app.route('/subscribe', methods=['POST'])
def subscribe():

    """
        Allows user to enter email address for subscription to newsletter.

        Fetch string data from website to MongoDB subscriptions collection.
        Insert a new entry in the MongoDB collection.

        Returns:
        template: redirect to index.html.

    """

    subscriptions = mongo.db.subscriptions
    return_data = request.form.to_dict()
    subscriptions.insert_one(return_data)

    return redirect(request.referrer)


# ======== COCKTAILS PAGE ======== #


# cocktails
@app.route("/get_cocktails")
def get_cocktails():

    """
        Get all cocktails from database displayed on several pages.

        Fetch categories from MongoDB categories collection.
        Fetch all cocktails options from MongoDB cocktail collection.
        Add pagination from page 1 to avoid content excess on page template.

        Returns:
        template: cocktails.html.

    """

    categories = list(mongo.db.categories.find())
    cocktails_collection = mongo.db.cocktails

    # fetch the page number from request / set the page 1
    page = int(request.args.get('page') or 1)
    num = 9

    # count documents for of pagination options
    count = ceil(float(cocktails_collection.count_documents({}) / num))

    # page - 1 checks that the first items can be found
    cocktails = list(
        cocktails_collection.find({}).skip((page - 1) * num).limit(num))

    return render_template(
        "cocktails.html", cocktails=cocktails,
        categories=categories, page=page, count=count, search=False)


# search box in cocktail.html
@app.route("/search", methods=["GET", "POST"])
def search():

    """
       Allows the user to search for filtered options on cocktail.html template

       4 options possible:
        - search by text input.
        - search by categories only.
        - search by text and categories.
        - neither (blank search)

       Returns:
       template: cocktail.html with filtered results

    """

    cursor = []

    if request.method == 'POST':

        # parse values from form
        search = request.form.get('search', None)
        select = request.form.get('select', None)

        # search only
        if search and select == 'All Categories':
            cursor = mongo.db.cocktails.find({'$text': {'$search': search}})

        # select only
        elif select != 'All Categories' and not search:
            cursor = mongo.db.cocktails.find({'category_name': select})

        elif search and select != 'All Categories':
            cursor = mongo.db.cocktails.find(
                {'$and':  [{'category_name': select},
                 {'$text': {'$search': search}}]})

        # no search and no select
        else:
            cursor = mongo.db.cocktails.find({})

    # parse filtered results
    cocktails = list(cursor)
    categories = list(mongo.db.categories.find())

    return render_template(
        "cocktails.html",
        cursor=cursor, cocktails=cocktails, categories=categories)


# ======== REGISTER PAGE ======== #


# register
@app.route("/register", methods=["GET", "POST"])
def register():

    """
        Displays register page to guest user and allows to create an account.

        Prevents duplication of username by checking users
        collection field "username".
        Stores informations from website form to MongoDB.
        Inserts a new entry in the users collection.

        Returns:
        template: redirect to profile.html if registration successful.

    """
    # if form is submitted
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # prevent username multiplication
        if existing_user:
            flash("Username already exists")

            return redirect(url_for("register"))

        # grabs data from form to users collection
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_img": request.form.get("user_img"),
            "user_level": request.form.get("user_level"),
            "user_loc": request.form.get("user_loc"),
            "liked_cocktail": []
        }
        mongo.db.users.insert_one(register)

        # inform user of successful registration
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")

        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# ======== LOGIN PAGE ======== #


# log in
@app.route("/login", methods=["GET", "POST"])
def login():

    """
        Displays log in page and allows user to log into account.

        Checks if the username exists in MongoDB users collection.
        Protect password confidentiality.
        Informs user if registration is successful or not through
        flash messages.

        Returns:
        template: profile.html if the registration is successful.
        template: login.html if registration unsuccessful.

    """

    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
          {"username": request.form.get("username").lower()})

        # grants profile page access to user
        if existing_user:

            if check_password_hash(
             existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Username doesn't exist")
            return redirect(url_for("login"))

    return render_template("login.html")


# ======== LOGOUT PAGE ======== #


# Allows registered user to log out from account
@app.route("/logout")
def logout():

    flash("You have been logged out")

    # removes session cookies
    session.pop("user")

    return redirect(url_for("login"))


# ======== PROFILE PAGE ======== #


# Displays profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    """
        Displays profile page with user informations to logged user.

        Fetch all user informations from MongoDB users collection.
        Checks previously submitted cocktails through username
        in cocktail collection.
        Grants access to all cocktail data to admin.
        Displays cocktail cards with pagination (6 per page).

        Parameter:
        string: username from user collection field "username".

        Returns:
        template: profile.html.

    """

    user = mongo.db.users.find_one({"username": username.lower()})

    # check for cocktails created by user / grant all access to admin
    if session["user"]:
        if session["user"] == "admin":
            cocktails = list(mongo.db.cocktails.find())
        else:
            cocktails = list(
                mongo.db.cocktails.find({"created_by": username.lower()}))

        # fetch the page number from request / set the page 1
        page = int(request.args.get('page') or 1)
        num = 6

        # count documents for of pagination options
        count = ceil(float(len(cocktails) / num))

        # page - 1 checks that the first items can be found
        start = (page - 1) * num
        end = start + num
        cocktails_display = cocktails[start:end]

        return render_template(
            "profile.html", user=user, cocktails=cocktails_display,
            page=page, count=count, search=False)

    return render_template(
        "profile.html", user=user, cocktails=cocktails)


# ======== EDIT PROFILE PAGE ======== #


# edit profile
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):

    """
        Allows the user to edit their profile through a form.

        Checks for username field in MongoDB field collection
        for editing rights.
        Displays (password, email and username not included)
        previously submitted data of the user.
        Fetch all new entries to database and update the fields
        when submitted.

        Parameter:
        string: username from users collection.

        Returns:
        template: edit_profile.html before changes if the user is logged in.
        template: profile.html after changes if the user is logged in.
        template: login.html if user not logged in.

    """

    user = mongo.db.users.find_one({"username": username.lower()})

    # update new field entries to database
    if request.method == "POST":
        submit = {
            "username": user["username"],
            "password": user["password"],
            "user_img": request.form.get("user_img"),
            "user_level": request.form.get("user_level"),
            "user_loc": request.form.get("user_loc"),
            "liked_cocktail": user["liked_cocktail"]
        }
        mongo.db.users.update({"username": username.lower()}, submit)
        flash("Voila! All new!")

        return redirect(url_for("profile", username=username))

    # check if user is logged in for security
    if "user" in session:
        return render_template("edit_profile.html", user=user)

    return redirect(url_for("login"))


# ======== DELETE PROFILE ======== #


# Allows user to delete account when in session
# Removes all user data from database
@app.route("/delete_profile/<username>")
def delete_profile(username):
    mongo.db.cocktails.remove({"created_by": username.lower()})
    mongo.db.users.remove({"username": username.lower()})
    flash("Profile deleted")
    session.pop("user")

    return redirect(url_for("register"))


# ======== ADD COCKTAIL PAGE ======== #


# add cocktail
@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():

    """
        Allows registered user to submit a cocktail to the website through
        a form.

        Allows all form fields to be sent to the MongoDB cocktail collection
        and category collection.
        Inserts a new entry in the previously mentionned collections.
        Prevents non-registered to have access to the page for security.

        Returns:
        template: add_cocktails.html before changes if the user is logged in.
        template: cocktails.html after changes if user is logged in.
        template: login.html is user is not logged in.

    """

    if request.method == "POST":

        date = str(datetime.date.today())
        print(date)
        # send form data to cocktails collection
        cocktail = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_description": request.form.get("cocktail_description"),
            "cocktail_img": request.form.get("cocktail_img"),
            "cocktail_ingredients": request.form.get("cocktail_ingredients"),
            "cocktail_instructions": request.form.get("cocktail_instructions"),
            "cocktail_prep": request.form.get("cocktail_prep"),
            "cocktail_diff": request.form.get("cocktail_diff"),
            "cocktail_serv": request.form.get("cocktail_serv"),
            "cocktail_img_cred": request.form.get("cocktail_img_cred"),
            "created_by": session["user"],
            "cocktail_like": 0,
            "cocktail_date": date
        }
        mongo.db.cocktails.insert_one(cocktail)
        flash("Merci for the new cocktail")

        return redirect(url_for("get_cocktails"))

    categories = mongo.db.categories.find()

    # check if the user is logged in
    if "user" in session:
        user = session["user"].lower()

        if user == session["user"].lower():
            return render_template("add_cocktail.html", categories=categories)

        # prevent other registered user access
        else:
            return redirect(url_for("index"))

    # prevent guest user access
    else:
        return redirect(url_for("login"))


# ======== EDIT COCKTAIL PAGE ======== #


# Displays edit cocktail pages
@app.route("/edit_cocktail/<cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):

    """
        Allows the user to edit their submitted cocktails through a form.

        Checks for cocktail ID field in MongoDB to fetch all data.
        Displays allpreviously submitted data of the cocktail by the user.
        Fetch all new entries to database and update the fields
        when submitted in cocktail collection.
        Checks if the user in session is the author of the entry.

        Parameter:
        ObjectId: cocktail_id from the cocktail collection ObjectId field.

        Returns:
        template: edit_cocktail.html before changes if the user is logged in.
        template: cocktails.html after changes if the user is logged in.
        template: index.html if the user is logged in but not the author.
        template: login.html if user not logged in.

    """
    cocktail_data = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})

    if request.method == "POST":

        # send form data to MongoDB and update fields
        submit = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_description": request.form.get("cocktail_description"),
            "cocktail_img": request.form.get("cocktail_img"),
            "cocktail_ingredients": request.form.get("cocktail_ingredients"),
            "cocktail_instructions": request.form.get("cocktail_instructions"),
            "cocktail_prep": request.form.get("cocktail_prep"),
            "cocktail_diff": request.form.get("cocktail_diff"),
            "cocktail_serv": request.form.get("cocktail_serv"),
            "cocktail_img_cred": request.form.get("cocktail_img_cred"),
            "created_by": session["user"],
            "cocktail_like": cocktail_data["cocktail_like"],
            "cocktail_date": cocktail_data["cocktail_date"]
        }
        mongo.db.cocktails.update({"_id": ObjectId(cocktail_id)}, submit)
        flash("Merci for the updated cocktail!")

        return redirect(url_for("get_cocktail", cocktail_id=cocktail_id))

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    # check if user in session is the author of the previous entries
    if "user" in session:
        user = session["user"].lower()

        if user == session["user"].lower():
            return render_template(
                "edit_cocktail.html", cocktail=cocktail, categories=categories)

        else:
            return redirect(url_for("index"))

    else:
        return redirect(url_for("login"))


# ======== COCKTAIL PAGE ======== #


# cocktail recipe
@app.route('/cocktail/<cocktail_id>')
def get_cocktail(cocktail_id):

    """
        Displays the data from cocktail collection to all users
        and display like button.

        Search through ObjectId field in MongoDB cocktail collection
        to fetch corresponding data.
        Checks if the logged in user has previously liked the cocktail
        through the user collection.
        Select 3 random cocktails of same category in suggested section.

        Parameter:
        ObjectId: cocktail_id from the cocktail collection ObjectId field.

        Returns:
        template: cocktail.html

    """

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    is_liked = False
    category = cocktail["category_name"]
    suggested_cocktails = list(
                mongo.db.cocktails.find({"category_name": category}))

    # removes current cocktail from suggested cocktails
    for i, item in enumerate(suggested_cocktails):
        if item["_id"] == ObjectId(cocktail_id):
            suggested_cocktails.pop(i)
            break

    # pick 3 random from suggested list
    random_cocktails = random.sample(suggested_cocktails, 3)

    # checks if cocktail was liked by registered user
    if "user" in session:
        user = session["user"].lower()
        user_data = mongo.db.users.find_one({"username": user})
        if cocktail_id in user_data["liked_cocktail"]:
            is_liked = True

    return render_template(
        "cocktail.html", cocktail=cocktail,
        is_liked=is_liked, suggested_cocktails=random_cocktails)


# like button
@app.route('/liked/<cocktail_id>', methods=["GET", "POST"])
def update_like(cocktail_id):

    """
        Allows registered user only  to use the like functionnality
        on the cocktail recipe page.

        Checks if the cocktail id was added to the liked_cocktail field
        in users collection to allow the access to like.
        Update the users and cocktail collections to keep like count and
        remove access to like to the user.

        Parameter:
        ObjectId: cocktail_id from the cocktail collection ObjectId field.

        Returns:
        template: cocktail.html when the button is clicked.

    """

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    user = session["user"].lower()
    user_data = mongo.db.users.find_one({"username": user})

    # allows to update users and cocktail collection
    # when like button is clicked
    if cocktail_id not in user_data["liked_cocktail"]:
        mongo.db.cocktails.update({
                "_id": ObjectId(cocktail_id)},
                {"$set": {"cocktail_like": cocktail["cocktail_like"] + 1}})
        mongo.db.users.update({
                "username": user},
                {"$push": {"liked_cocktail": cocktail_id}})
        cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})

    flash("Merci for le like!")

    return render_template(
        "cocktail.html", cocktail=cocktail,
        is_liked=True)


# ======== DELETE COCKTAIL ======== #


# Allows the user(author/admin) to delete cocktail
@app.route("/delete_cocktail/<cocktail_id>")
def delete_cocktail(cocktail_id):
    mongo.db.cocktails.remove({"_id": ObjectId(cocktail_id)})
    flash("Adieu cocktail, see you never!")

    return redirect(url_for("get_cocktails"))


# ======== CATEGORY PAGE ======== #


# categories
@app.route("/get_categories")
def get_categories():

    """
        Display all categories for the admin only.

        Fetch the list of all categories in the MongoDB categories collection.

        Returns:
        template: categories.html if admin is logged in.
        template: index.html in any other case.

    """

    categories = list(
                mongo.db.categories.find().sort("category_name", 1))

    if "user" in session.keys():
        if session["user"] == "admin":
            return render_template(
                "categories.html", categories=categories)

    return redirect(url_for("index"))


# ======== EDIT CATEGORY PAGE ======== #


# edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    """
        Allows the admin to edit a category through a form.

        Checks for category ID field in MongoDB to fetch relative data.
        Displays previously submitted data regarding the category by admin.
        Fetch changes to database and update the fields
        when submitted in category collection.
        Checks if the user in session is the admin.

        Parameter:
        ObjectId: category_id from the category collection ID field.

        Returns:
        template: edit_categories.html for the admin
        before submitting changes
        template: categories.html after submitting changes
        if the user is the admin.
        template: index.html if the user is logged in but not the admin.
        template: login.html if user not logged in.

    """

    if request.method == "POST":
        # send form data to MongoDB collection and update the field
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Voila! All new!")

        return redirect(url_for("get_categories"))

    # find category id in category collection
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    # allow access to admin and protect access from other users
    if "user" in session:
        user = session["user"].lower()

        if user == "admin":
            return render_template("edit_category.html", category=category)

        else:
            return redirect(url_for("index"))

    else:
        return redirect(url_for("login"))


# ======== ADD CATEGORY PAGE ======== #


# add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    """
        Allows admin to submit a category to the website through
        a form.

        Allows the form field to be sent to the MongoDB category collection
        Inserts a new entry in the previously mentionned collection.
        Prevents non-registered to have access to the page for security.

        Returns:
        template: add_categories.html if user is admin
        before submitting.
        template: categories.html after submitting if user is admin
        template: login.html if user is not admin.

    """

    if request.method == "POST":

        # send form data to MongoDB collection and insert new entry
        category = {
            "category_name": request.form.get("category_name"),
        }
        mongo.db.categories.insert_one(category)
        flash("Merci for the new category")

        return redirect(url_for("get_categories"))

    categories = mongo.db.categories.find()

    # grants access to admin and protect from other user access
    if "user" in session:
        user = session["user"].lower()

        if user == "admin".lower():
            return render_template("add_category.html", categories=categories)
        else:
            return redirect(url_for("index"))

    else:
        return redirect(url_for("login"))


# ======== DELETE CATEGORY ======== #


# allows admin to a delete category forever
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Adieu Category, see you never!")

    return redirect(url_for("get_categories"))


# ======== USER LIST ======== #

# all users list for admin
@app.route("/users_list")
def users_list():

    """
        Display all users for the admin only.

        Fetch the list of all users per username
        in the MongoDB users collection.
        Displays users with pagination (10 per page)
        Exclude Admin from list.

        Returns:
        template: users_list.html if admin is logged in.
        template: index.html in any other case.

    """
    users = list(
                mongo.db.users.find().sort("username", 1))

    # exclude admin from the list by finding
    # the dictionary where username is admin
    for i, user in enumerate(users):
        if user["username"] == "admin":
            users.pop(i)
            break

    # fetch the page number from request / set the page 1
    page = int(request.args.get('page') or 1)
    num = 10

    # count documents for of pagination options
    count = ceil(float(len(users) / num))

    # page - 1 checks that the first items can be found
    start = (page - 1) * num
    end = start + num
    users_display = users[start:end]

    # grants list access to admin only
    if "user" in session.keys():
        if session["user"] == "admin":
            return render_template(
                "users_list.html", users=users_display, user_count=len(users),
                page=page, count=count, search=False)

    return redirect(url_for("index"))


# ======== DELETE USER ======== #


# Allows admin to delete user account when in session
# Removes all user data from database
@app.route("/delete_user/<username>")
def delete_user(username):
    mongo.db.cocktails.remove({"created_by": username.lower()})
    mongo.db.users.remove({"username": username.lower()})
    flash("Adieu user!")

    return redirect(url_for("users_list"))


# ======== ERROR PAGES ======== #


# Displays 404 error page
@ app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


# Displays 505 error page
@ app.errorhandler(505)
def internal(error):
    return render_template('errors/404.html'), 505


# ============================================ #


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
