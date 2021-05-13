import os
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env 


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", page_title="Recipes")


@app.route("/login")
def login():
    return render_template("login.html", page_title="Log In")


@app.route("/register")
def register():
    return render_template("register.html", page_title="Register")
    

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0,0,0,0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)