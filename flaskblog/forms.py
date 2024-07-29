from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.validators import (
    validate_username,
    validate_email,
    update_validation_username,
    update_validation_email
)


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=2, max=20), validate_username]
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


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=2, max=20), update_validation_username]
    )
    email = StringField(
        "E-mail",
        validators=[DataRequired(), Email(), update_validation_email]
    )
    picture = FileField(
        "Update profile picture",
        validators=[FileAllowed(['jpg', 'jpeg', 'png',])]
    )
    submit = SubmitField(
        "Update"
    )


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")
