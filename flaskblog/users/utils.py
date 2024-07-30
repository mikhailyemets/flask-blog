from flask_mail import Message
from flask import url_for
from flaskblog import app, mail
from flaskblog.models import User
import os
import secrets
from PIL import Image

def send_reset_email(user: User) -> None:
    token = user.get_reset_token()
    reset_url = url_for("users.reset_token", token=token, _external=True)
    msg = Message(
        "Password reset request",
        sender="noreply@demo.com",
        recipients=[user.email]
    )
    msg.body = f"""
    Hi,

    We received a request to reset your password. You can reset your password by clicking the link below:

    {url_for("users.reset_token", token=token, external=True)}

    If you did not request this password reset, please ignore this email. Your password will not be changed.

    Thank you,
    The FlaskBlog Team
    """
    msg.html = f"""
       <p>Hi,</p>
       <p>We received a request to reset your password. You can reset your password by clicking the link below:</p>
       <p><a href="{reset_url}">Reset Password</a></p>
       <p>If you did not request this password reset, please ignore this email. Your password will not be changed.</p>
       <p>Thank you,<br>The FlaskBlog Team</p>
       """
    mail.send(msg)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path,
        "static/profile_pics",
        picture_filename
    )

    #resing big pictures to keep it small
    output_size = (125,125)
    input_ = Image.open(form_picture)
    input_.thumbnail(output_size)

    input_.save(picture_path)
    return picture_filename