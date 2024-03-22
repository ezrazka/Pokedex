from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired
from wtforms.validators import Email, EqualTo

from application.utils import exists_email, not_exists_email, exists_username

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Enter your username"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

class SignUpForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired(), exists_username])
    email               = EmailField("email", validators=[DataRequired(), Email(), exists_email])
    password            = PasswordField("password", validators=[DataRequired()])
    confirm_password    = PasswordField("confirm password", validators=[DataRequired(), EqualTo("password")])
    submit              = SubmitField("sign up")