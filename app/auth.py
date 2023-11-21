from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
)
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    # TODO login code here
    pass


@auth.route("/signup")
def signup():
    return render_template("register.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    # TODO signup code here
    pass


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
