from flask import Flask

# import config file
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

server = Flask(__name__)
server.config.from_object(Config)

db = SQLAlchemy(server)
migrate = Migrate(server, db)

login = LoginManager(server)

from server import routes, models
