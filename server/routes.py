from flask import render_template, send_from_directory, request, redirect, flash, url_for
from server import server
from server.forms import LoginForm, CreateAcctForm

from flask_login import current_user, login_user, logout_user
from server.models import User

import os, requests

# serve main files
@server.route("/")
def index():
    return render_template("index.html")


# serve search page
@server.route("/search", methods=["GET", "POST"])
def search():
    resp = requests.get(
        "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&apikey="
        + server.config['AV_API_KEY']
        + "&keywords="
        + request.form["query"]
    )
    json = resp.json()["bestMatches"]

    return render_template("search.html", query=request.form["query"], results=json)


@server.route("/settings")
def settings():
    return render_template("settings.html")


@server.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.rememberme.data)
        flash('Logged in as ' + user.username)
        return redirect(url_for("index"))
    
    return render_template("login.html", form=form)

@server.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@server.route("/createacct", methods=["GET", "POST"])
def createacct():
    form = CreateAcctForm()
    if form.validate_on_submit():
        print("ACCOUNT CREATE with:")
        print("username: " + form.username.data)
        print("password: " + form.password.data)
        print("avatar: " + form.avatar.data)
        return redirect(url_for("index"))

    return render_template("createacct.html", form=form)


# serve favicons
@server.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(server.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@server.route("/favicon-16x16.png")
def favicon16():
    return send_from_directory(
        os.path.join(server.root_path, "static"),
        "favicon-16x16.png",
        mimetype="image/vnd.microsoft.icon",
    )


@server.route("/favicon-32x32.png")
def favicon32():
    return send_from_directory(
        os.path.join(server.root_path, "static"),
        "favicon-32x32.png",
        mimetype="image/vnd.microsoft.icon",
    )
