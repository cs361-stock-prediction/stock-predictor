from flask import (
    render_template,
    send_from_directory,
    request,
    redirect,
    flash,
    url_for,
)
from server import server, db
from server.forms import LoginForm, CreateAcctForm

from flask_login import current_user, login_user, logout_user, login_required
from server.models import User

import plotly.graph_objects as go

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
        + server.config["AV_API_KEY"]
        + "&keywords="
        + request.form["query"]
    )
    json = resp.json()["bestMatches"]

    return render_template("search.html", query=request.form["query"], results=json)

@server.route("/prediction/<stock>")
def prediction(stock):

    # Collect data about stock

    resp = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
            + str(stock)
            + "&outputsize=compact&datatype=json&apikey="
            + server.config["AV_API_KEY"])

    # Convert data to python iterable format

    json = resp.json()

    data = []
    date = []
    for day in json['Time Series (Daily)']:
        data.append(float(json['Time Series (Daily)'][day]['4. close']))
        date.append(day)
    
    data.reverse()
    date.reverse()

    print (data)
    print (date)
    
    # Generate trendline




    #turn dates to x values:

    import datetime

    datemask = "%Y-%m-%d"

    datetimes = [datetime.datetime.strptime(x, datemask) for x in date]

    base = datetimes[0]


    x = [0]
    [x.append((d1 - base).days) for d1 in datetimes[1:]]

    
    slope = ((data[-10] - data[-1]) / (x[-10] - x[-1]))

    x1 = [x[-1]]
    d1 = [data[-1]]

    for n in range(0, 10):
        d1.append(d1 [-1] + (1 * slope))
        x1.append(x1[-1] +1)


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=data, name='Raw Data Graph',
                            line=dict(color='royalblue', width=3)))
    fig.add_trace(go.Scatter(x=x1, y=d1, name='Porj Graph',
                            line=dict(color='aqua', width=3)))

    fig.show()



    # Extrapolate Data

    

    return render_template("prediction.html", stock=stock)


@server.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.rememberme.data)
        flash("Logged in as " + user.name())

        # go to previous page if login used as interstitial, otherwise /
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)

    return render_template("login.html", form=form)


@server.route("/logout")
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("index"))


@server.route("/createacct", methods=["GET", "POST"])
def createacct():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = CreateAcctForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, displayname=form.displayname.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Registered new user " + new_user.name())
        login_user(new_user)
        return redirect(url_for("index"))

    return render_template("createacct.html", form=form)


@server.route("/settings")
@login_required
def settings():
    return render_template("settings.html")


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
