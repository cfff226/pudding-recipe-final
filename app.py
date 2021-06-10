import os
from flask import (
    Flask, render_template, request, flash,
    redirect, session, url_for)
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


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", page_title="Home")

# Retrieve recipe data from mongodb
@app.route("/get_recipes")
def get_recipes():
    recipe = list(mongo.db.recipes.find())
    print(recipe)
    return render_template("recipes.html", recipes=recipe)


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", page_title="Recipes")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Make sure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login", _external=True, _scheme='https'))

        else:
            # Username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login", _external=True, _scheme='https'))

    return render_template("login.html", page_title="Log In")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session user's Username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # Display all of users recipes
        return render_template("profile.html",
                               username=username,
                               recipes=recipes)

    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Get users form input and send to database
    if request.method == "POST":
        dessert_ingredients = request.form.getlist("dessert_ingredients")
        ingredients_list = []
        for ingredients in dessert_ingredients:
            ingredients_list.append(ingredients)
        dessert_instructions = request.form.getlist("dessert_instructions")
        instructions_list = []
        for instructions in dessert_instructions:
            instructions_list.append(instructions)
        dessert_recipe = {
            "dessert_name": request.form.get("dessert_name"),
            "dessert_image": request.form.get("dessert_image"),
            "dessert_ingredients": ingredients_list,
            "dessert_instructions": instructions_list,
            "created_by": session["user"]
        }
        # Post users input to Mongodb
        mongo.db.recipes.insert_one(dessert_recipe)
        flash("Thanks! Your recipe has been added")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("add_recipe.html")


<<<<<<< HEAD
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.tasks.find_one({"_id": ObjectId(recipe_id)})
=======
@app.route("/edit_task/<task_id>", methods=["GET, POST"]
def edit_task(task_id):
    task = mongo.db.tasks.find_one({"id: ObjectId(task_id)")})
>>>>>>> 61cb2d9d7691c3e4e0e37c8555ffdb21a9b64119


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html", page_title="Register")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0,0,0,0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
