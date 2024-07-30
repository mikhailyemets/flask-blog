import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.filters import safe_truncate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# add func for safe truncate of words
app.jinja_env.filters["safe_truncate"] = safe_truncate

# to make account login required
login_manager.login_view = "login"

# to make nice message about login in
login_manager.login_message_category = "info"

from flaskblog import routes