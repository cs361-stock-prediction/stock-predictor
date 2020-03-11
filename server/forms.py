from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FileField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            InputRequired(),
            Length(min=4, max=15, message="Username must be 4 to 15 characters long"),
        ],
    )
    password = PasswordField("Password", validators=[InputRequired()])
    rememberme = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class CreateAcctForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            InputRequired(),
            Length(min=4, max=15, message="Username must be 4 to 15 characters long"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(min=8, max=50, message="Password must be 8 to 50 characters long"),
        ],
    )
    passconfirm = PasswordField(
        "Re-type password",
        validators=[
            InputRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    avatar = FileField("Avatar")
    submit = SubmitField("Create Account")
