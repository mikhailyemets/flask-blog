import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.filters import safe_truncate
from flask_mail import Mail

app = Flask(__name__)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



# add func for safe truncate of words
app.jinja_env.filters["safe_truncate"] = safe_truncate

# to make account login required
login_manager.login_view = "users.login"

# to make nice message about login in
login_manager.login_message_category = "info"

# Blueprints configuration
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

mail = Mail(app)
