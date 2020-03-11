import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my-name-a-borat"
    AV_API_KEY = "2T50TIVI1285LSG4"

    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or "mysql+pymysql://cs361_detjensr:i-get-clock-radio@classmysql.engr.oregonstate.edu:3306/cs361_detjensr"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
