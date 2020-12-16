import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():
    cocktails = list(mongo.db.cocktails.find())
    return render_template("index.html", cocktails=cocktails)


@app.route("/get_cocktails")
def get_cocktails():
    cocktails = list(mongo.db.cocktails.find())
    return render_template("cocktails.html", cocktails=cocktails)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    cocktails = list(mongo.db.cocktails.find({"$text": {"$search": query}}))
    return render_template("cocktails.html", cocktails=cocktails)


@app.route("/register", methods=["GET", "POST"])
def register():
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
            "user_loc": request.form.get("user_loc")
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user_data = username = mongo.db.users.find_one(
        {"username": session["user"]})
    username = user_data["username"]
    user_img = user_data["user_img"]
    user_level = user_data["user_level"]
    user_loc = user_data["user_loc"]

    if session["user"]:
        if session["user"] == "admin":
            cocktails = list(mongo.db.cocktails.find())
        else:
            cocktails = list(
                mongo.db.cocktails.find({"created_by": username.lower()}))

        return render_template(
            "profile.html", username=username,
            cocktails=cocktails, user_img=user_img,
            user_level=user_level, user_loc=user_loc)

    return render_template(
        "profile.html", username=username)


@app.route("/delete_profile/<username>")
def delete_profile(username):
    mongo.db.users.remove({"username": username.lower()})
    flash("Profile deleted")
    session.pop("user")

    return redirect(url_for("register"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():
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
            "cocktail_like": request.form.get("cocktail_like")
        }
        mongo.db.cocktails.insert_one(cocktail)
        flash("Merci for the new cocktail")
        return redirect(url_for("get_cocktails"))

    categories = mongo.db.categories.find()
    if "user" in session:
        user = session["user"].lower()
        if user == session["user"].lower():
            return render_template("add_cocktail.html", categories=categories)
        else:
            return redirect(url_for("index"))

    else:
        return redirect(url_for("login"))


@app.route("/edit_cocktail/<cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):
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
            "cocktail_like": request.form.get("cocktail_like")
        }
        mongo.db.cocktails.update({"_id": ObjectId(cocktail_id)}, submit)
        flash("Merci for the updated cocktail!")

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


@app.route('/cocktail/<cocktail_id>')
def get_cocktail(cocktail_id):
    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    if "user" in session:
        user = session["user"].lower()
        print(user)

    return render_template(
        "cocktail.html", cocktail=cocktail,)


@app.route("/delete_cocktail/<cocktail_id>")
def delete_cocktail(cocktail_id):
    mongo.db.cocktails.remove({"_id": ObjectId(cocktail_id)})
    flash("Adieu cocktail, see you never!")
    return redirect(url_for("get_cocktails"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


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


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Adieu Category, see you never!")
    return redirect(url_for("get_categories"))


@ app.route('/subscribe', methods=['POST'])
def subscribe():
    subscriptions = mongo.db.subscriptions
    return_data = request.form.to_dict()
    subscriptions.insert_one(return_data)
    return redirect(request.referrer)


@ app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@ app.errorhandler(505)
def internal(error):
    return render_template('errors/404.html'), 505


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
