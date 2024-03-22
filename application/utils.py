from application.models import User
from flask import current_app

from wtforms.validators import ValidationError

def exists_email(form, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError("Email already exists. Please user a different email :)")

def not_exists_email(form, email):
    user = User.query.filter_by(email=email.data).first()
    if not user:
        raise ValidationError("Email not found :(")

def exists_username(form, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError("Username already exists. Please use a different username :)")