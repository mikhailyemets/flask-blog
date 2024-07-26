from flask import Flask, render_template, url_for, flash, redirect
from dotenv import load_dotenv
import os
from forms import RegistrationForm, LoginForm


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

posts = [
    {
        "author": "Michael",
        "title": "Blog Post 1",
        "content": "Very first post on this flask app",
        "date_posted": "July 29, 2024"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Very second post on this flask app",
        "date_posted": "June 30, 2024"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="About")


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"{form.email.data} have been successfully logged in!", category="success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful! Check you credentials!", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)