from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from application import app
from application.models import User
from application.forms import LoginForm


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("profile", username=current_user.username))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and password == user.password:
            login_user(user)
            return redirect(url_for("index"))
        else:
            return redirect(url_for("login"))
    
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    pass

@app.route("/")
# @login_required
def index():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")

if __name__ == "__main__":
    app.run(debug=True)