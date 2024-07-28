from wtforms.validators import ValidationError
from flaskblog.models import User
from flaskblog import app


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
