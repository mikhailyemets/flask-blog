from flask_mail import Message
from flask import url_for
from flaskblog import mail
from flaskblog.models import User


def send_reset_email(user: User) -> None:
    token = user.get_reset_token()
    reset_url = url_for("reset_token", token=token, _external=True)
    msg = Message(
        "Password reset request",
        sender="noreply@demo.com",
        recipients=[user.email]
    )
    msg.body = f"""
    Hi,

    We received a request to reset your password. You can reset your password by clicking the link below:

    {url_for("reset_token", token=token, external=True)}

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
