from flask import render_template, send_from_directory, request, redirect
from server import server
from server.forms import LoginForm, CreateAcctForm

import os, requests

# serve main files
@server.route("/")
def index():
    return render_template("index.html")

# serve search page
@server.route("/search", methods=['GET', 'POST'])
def search():
    resp = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&apikey=' + Config.AV_API_KEY + '&keywords=' + request.form['query'])
    json = resp.json()['bestMatches']

    return render_template("search.html", query=request.form['query'], results=json)


@server.route("/settings")
def settings():
    return render_template("settings.html")


@server.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('LOGIN with:')
        print('username: ' + form.username.data)
        print('password: ' + form.password.data)
        print('remember: ' + str(form.rememberme.data))
        return redirect('/')

    return render_template("login.html", form=form)


@server.route("/createacct", methods=['GET', 'POST'])
def createacct():
    form = CreateAcctForm()
    if form.validate_on_submit():
        print('ACCOUNT CREATE with:')
        print('username: ' + form.username.data)
        print('password: ' + form.password.data)
        print('avatar: ' + form.avatar.data)
        return redirect('/')

    return render_template("createacct.html", form=form)

# serve favicons
@server.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(server.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@server.route('/favicon-16x16.png')
def favicon16():
    return send_from_directory(os.path.join(server.root_path, 'static'), 'favicon-16x16.png', mimetype='image/vnd.microsoft.icon')


@server.route('/favicon-32x32.png')
def favicon32():
    return send_from_directory(os.path.join(server.root_path, 'static'), 'favicon-32x32.png', mimetype='image/vnd.microsoft.icon')
