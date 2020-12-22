import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from math import ceil
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# ======== INDEX PAGE ======== #


# Display cocktails in index page
@app.route('/')
def index():
    """
        Returns the list of all cocktails in cocktail collection from database
        to be rendered in the template index.html
    """

    cocktails = list(mongo.db.cocktails.find())
    return render_template("index.html", cocktails=cocktails)


# Subscribe box
@ app.route('/subscribe', methods=['POST'])
def subscribe():
    """
        Fetch data to database and stores in collection
        for future use.
    """

    subscriptions = mongo.db.subscriptions
    return_data = request.form.to_dict()
    subscriptions.insert_one(return_data)

    return redirect(request.referrer)


# ======== COCKTAIL PAGE ======== #


# Get all cocktails from database
@app.route("/get_cocktails")
def get_cocktails():
    """
        Add pagination from page 1 to avoid content excess on page template.
        Fetch all cocktails options from database.
        Renders cocktails vith pagination options.
    """

    categories = list(mongo.db.categories.find())
    cocktails_collection = mongo.db.cocktails

    # get the page number from request or set the page 1 if first page
    page = int(request.args.get('page') or 1)
    num = 2

    # count documents to calculate number of pagination options
    count = ceil(int(cocktails_collection.count_documents({}) / num))

    # page - 1 ensures that the first items can be found
    cocktails = list(
        cocktails_collection.find({}).skip((page - 1) * num).limit(num))

    return render_template(
        "cocktails.html", cocktails=cocktails,
        categories=categories, page=page, count=count, search=False)


# search box in cocktail.html
@app.route("/search", methods=["GET", "POST"])
def search():
    """
       Allows the user to search cocktails by:
        - just text input
        - text input and category
        - just category
       Returns filtered results
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

    cocktails = list(cursor)
    categories = list(mongo.db.categories.find())

    return render_template(
        "cocktails.html",
        cursor=cursor, cocktails=cocktails, categories=categories)


# ======== REGISTER PAGE ======== #


# Displays register page
@app.route("/register", methods=["GET", "POST"])
def register():
    """
        Allows new user to register to access profile page.
        Prevents multiplication of username.
        Stores informations to database.
        Redirects to profile page.
    """

    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")

            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_img": request.form.get("user_img"),
            "user_level": request.form.get("user_level"),
            "user_loc": request.form.get("user_loc"),
            "liked_cocktail": []
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")

        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# ======== LOGIN PAGE ======== #


# Displays log in page
@app.route("/login", methods=["GET", "POST"])
def login():
    """
        Allows registered user to access profile page through username.
        Protect password confidentiality.
        Informs user if incorrect entry.
        Fetch all previous informations linked to user.
        Redirects to profile page.
    """

    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
          {"username": request.form.get("username").lower()})

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
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# ======== LOGOUT PAGE ======== #


# Allows registered user to log out from account
@app.route("/logout")
def logout():

    flash("You have been logged out")
    session.pop("user")

    return redirect(url_for("login"))


# ======== PROFILE PAGE ======== #


# Displays profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
        Fetches all user informations through username, including previously
        submited cocktails and renders on profile page.
        Allows admin to access category data.
    """

    user = mongo.db.users.find_one({"username": username.lower()})

    if session["user"]:
        if session["user"] == "admin":
            cocktails = list(mongo.db.cocktails.find())
        else:
            cocktails = list(
                mongo.db.cocktails.find({"created_by": username.lower()}))

        return render_template("profile.html", user=user, cocktails=cocktails)

    return render_template(
        "profile.html", user=user, cocktails=cocktails)


# ======== EDIT PROFILE PAGE ======== #


# Displays edit profile page
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):

    """
        If the user has logged in
       Fetch all user information and displays it in a form,
       Allows modifications.
       If user is not logged in, redirect to login page
    """

    user = mongo.db.users.find_one({"username": username.lower()})

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

    if "user" in session:
        return render_template("edit_profile.html", user=user)

    return redirect(url_for("login"))


# Allows user to delete account.
# Removes all data from database
@app.route("/delete_profile/<username>")
def delete_profile(username):
    mongo.db.users.remove({"username": username.lower()})
    flash("Profile deleted")
    session.pop("user")

    return redirect(url_for("register"))


# ======== ADD COCKTAIL PAGE ======== #


# Displays add cocktail page
@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():

    """
        If the cocktail was submitted by the registered user:
        Allows registered user to access change previous cocktail data entries.
        Fetch all previous informations linked to cocktail.
        Redirects to cocktails page.
    """

    if request.method == "POST":

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
            "cocktail_like": 0
        }
        mongo.db.cocktails.insert_one(cocktail)
        flash("Merci for the new cocktail")

        return redirect(url_for("get_cocktails"))

    categories = mongo.db.categories.find()

    if "user" in session:
        user = session["user"].lower()

        if user == session["user"].lower():
            return render_template("add_cocktail.html", categories=categories)

        #prevent other registered user to submit changes
        else:
            return redirect(url_for("index"))

    #prevent guest user to submit changes
    else:
        return redirect(url_for("login"))


# ======== EDIT COCKTAIL PAGE ======== #


# Displays edit cocktail pages
@app.route("/edit_cocktail/<cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):
    cocktail_data = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})

    if request.method == "POST":

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
            "cocktail_like": cocktail_data["cocktail_like"]
        }
        mongo.db.cocktails.update({"_id": ObjectId(cocktail_id)}, submit)
        flash("Merci for the updated cocktail!")

        return redirect(url_for("get_cocktail", cocktail_id=cocktail_id))

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

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


# Display cocktail recipe page
@app.route('/cocktail/<cocktail_id>')
def get_cocktail(cocktail_id):

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    is_liked = False

    if "user" in session:

        user = session["user"].lower()
        user_data = mongo.db.users.find_one({"username": user})
        if cocktail_id in user_data["liked_cocktail"]:
            is_liked = True

    return render_template(
        "cocktail.html", cocktail=cocktail,
        is_liked=is_liked)


# Allows like button functionnality
@app.route('/liked/<cocktail_id>', methods=["GET", "POST"])
def update_like(cocktail_id):

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    user = session["user"].lower()
    user_data = mongo.db.users.find_one({"username": user})

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


# delete cocktail
@app.route("/delete_cocktail/<cocktail_id>")
def delete_cocktail(cocktail_id):
    mongo.db.cocktails.remove({"_id": ObjectId(cocktail_id)})
    flash("Adieu cocktail, see you never!")

    return redirect(url_for("get_cocktails"))


# ======== CATEGORY PAGE ======== #


# Displays categories page
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))

    return render_template("categories.html", categories=categories)


# ======== EDIT CATEGORY PAGE ======== #


# Displays edit category page
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Another category added!")

        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    if "user" in session:
        user = session["user"].lower()

        if user == "admin":
            return render_template("edit_category.html", category=category)

        else:
            return redirect(url_for("index"))

    else:
        return redirect(url_for("login"))


# ======== ADD CATEGORY PAGE ======== #

# Displays add category page
@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    if request.method == "POST":

        category = {
            "category_name": request.form.get("category_name"),
        }
        mongo.db.categories.insert_one(category)
        flash("Merci for the new category")

        return redirect(url_for("get_categories"))

    categories = mongo.db.categories.find()

    if "user" in session:
        user = session["user"].lower()

        if user == "admin".lower():
            return render_template("add_category.html", categories=categories)

    else:
        return redirect(url_for("login"))


# ======== DELETE CATEGORY ======== #


# delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Adieu Category, see you never!")

    return redirect(url_for("get_categories"))


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
            debug=True)
