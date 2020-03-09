import os
import requests

from flask import Flask, render_template, send_from_directory, request, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FileField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo

import flask_login

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15, message='Username must be 4 to 15 characters long')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=50, message='Password must be 8 to 50 characters long')])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    
class CreateAcctForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15, message='Username must be 4 to 15 characters long')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=50, message='Password must be 8 to 50 characters long')])
    passconfirm = PasswordField('Re-type password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    avatar = FileField('Avatar')
    submit = SubmitField('Create Account')

# for login: https://www.youtube.com/watch?v=8aTnmsDMldY

webserver = Flask(__name__)
webserver.config['SECRET_KEY'] = 'my-name-a-borat'

API_KEY = '2T50TIVI1285LSG4'

# serve main files
@webserver.route("/")
def index():
    return render_template("index.html")

# serve search page
@webserver.route("/search", methods=['GET', 'POST'])
def search():
    resp = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&apikey=' + API_KEY + '&keywords=' + request.form['query'])
    json = resp.json()['bestMatches']

    return render_template("search.html", query=request.form['query'], results=json)


@webserver.route("/settings")
def settings():
    return render_template("settings.html")


#  ~ @webserver.route("/login")
#  ~ def login():
    #  ~ form = LoginForm()
    
    #  ~ return render_template("login.html", form=form)
    
    
@webserver.route("/login", methods=['GET', 'POST'])
def login():
    login = LoginForm()
    create = CreateAcctForm()
    if login.validate_on_submit():
        print('LOGIN with:')
        print('username: ' + login.username.data)
        print('password: ' + login.password.data)
        return redirect('/')
    if create.validate_on_submit():
        print('ACCOUNT CREATE with:')
        print('username: ' + create.username.data)
        print('password: ' + create.password.data)
        return redirect('/')

    return render_template("login-new.html", login=login, create=create)

# serve favicons
@webserver.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(webserver.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@webserver.route('/favicon-16x16.png')
def favicon16():
    return send_from_directory(os.path.join(webserver.root_path, 'static'), 'favicon-16x16.png', mimetype='image/vnd.microsoft.icon')


@webserver.route('/favicon-32x32.png')
def favicon32():
    return send_from_directory(os.path.join(webserver.root_path, 'static'), 'favicon-32x32.png', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    webserver.run(debug=True, host="0.0.0.0", port=4096)
