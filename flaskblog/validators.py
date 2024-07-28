from wtforms.validators import ValidationError
from flaskblog.models import User
from flaskblog import app
from flask_login import current_user


def validate_username(form, field):
    with app.app_context():
        user = User.query.filter_by(username=field.data).first()
    if user:
        raise ValidationError("Username is already taken!")


def validate_email(form, field):
    with app.app_context():
        user = User.query.filter_by(email=field.data).first()
    if user:
        raise ValidationError("Email is already taken!")


def update_validation_username(form, field):
    if field.data != current_user.username:
        with app.app_context():
            user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError("Username is already taken!")


def update_validation_email(form, field):
    if field.data != current_user.email:
        with app.app_context():
            user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError("Email is already taken!")