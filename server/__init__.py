from flask import Flask

# import config file
from config import Config

#  ~ import flask_login
#  ~ login_manager = flask_login.LoginManager()

#  ~ from flask_sqlalchemy import SQLAlchemy
#  ~ from flask_migrate import Migrate

server = Flask(__name__)
server.config.from_object(Config)

#  ~ db = SQLAlchemy(server)
#  ~ migrate = Migrate(server, db)

from server import routes
