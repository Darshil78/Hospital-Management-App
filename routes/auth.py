from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from extensions import db
from models.user import User


auth = Blueprint(
    "auth",
    __name__
)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = (request.form.get("role") or "Patient").strip().capitalize()

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered")
            return redirect(url_for("auth.register"))

        user = User(
            name=name,
            email=email,
            password=generate_password_hash(password),
            role=role,
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful")

        if role == "Admin":
            return redirect(url_for("auth.admin_login"))

        return redirect(url_for("auth.login"))

    return render_template("register.html", admin_mode=False)


@auth.route("/admin/register", methods=["GET", "POST"])
def admin_register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered")
            return redirect(url_for("auth.admin_register"))

        user = User(
            name=name,
            email=email,
            password=generate_password_hash(password),
            role="Admin",
        )

        db.session.add(user)
        db.session.commit()

        flash("Admin registration successful")
        return redirect(url_for("auth.admin_login"))

    return render_template("register.html", admin_mode=True)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful")
            return redirect(url_for("dashboard.home"))

        flash("Invalid email or password")

    return render_template("login.html", admin_mode=False)


@auth.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password) and (user.role or "").capitalize() == "Admin":
            login_user(user)
            flash("Admin login successful")
            return redirect(url_for("dashboard.home"))

        flash("Invalid admin credentials")

    return render_template("login.html", admin_mode=True)


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("auth.login"))