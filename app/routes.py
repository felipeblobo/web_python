from app import app
from flask import render_template, request


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Felipe"}
    posts = [
        {
            "author": {"username": "Felipe"},
            "body": "Olá moça"

        },

        {
            "author": {"username": "Pedro"},
            "body": "Olá pessoal!"

        }
    ]
    return render_template("index.html", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.values.get("user"))
    return render_template("login.html", title="login")
