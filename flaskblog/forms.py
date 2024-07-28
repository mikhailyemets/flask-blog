from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.validators import validate_username, validate_email

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min:=2, max=20), validate_username]
    )
    email = StringField(
        "E-mail",
        validators=[DataRequired(), Email(), validate_email]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )
    confirm_password = PasswordField(
        "Confirm password",
        validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField(
        "Sign up"
    )


class LoginForm(FlaskForm):
    email = StringField(
        "E-mail",
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )
    remember = BooleanField(
        "Remember me"
    )
    submit = SubmitField(
        "Sign in"
    )
