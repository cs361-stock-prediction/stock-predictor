from server import db, login

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    displayname = db.Column(db.String(64))
    password = db.Column(db.String(128), nullable=False)
    avatar = db.Column(db.String(128))
    favorites = db.Column(db.PickleType())
    history = db.Column(db.PickleType())

    def __repr__(self):  # toString()
        return "<User {}>".format(self.username)
        
    def get_avatar(self):
        return "/static/avatars/" + self.avatar if self.avatar else "/static/default.png"

    def name(self):
        return self.displayname or self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
