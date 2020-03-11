from server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128))
    avatar = db.Column(db.LargeBinary())
    favorites = db.Column(db.PickleType())
    history = db.Column(db.PickleType())
	
    def __repr__(self):
        return '<User {}>'.format(self.username)   
