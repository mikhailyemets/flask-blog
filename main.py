from flask import Flask, render_template, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

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


if __name__ == "__main__":
    app.run(debug=True)