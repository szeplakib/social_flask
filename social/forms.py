from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, Optional


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn btn-success btn-block'})


class RegisterForm(FlaskForm):
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [Length(min=3)])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    birthday = DateField('Birthday', [Optional()])
    submit = SubmitField('Resister', render_kw={'class': 'btn btn-success btn-block'})


class SearchForm(FlaskForm):
    search = StringField('search', [DataRequired()])
    submit = SubmitField('Search', render_kw={'class': 'btn btn-success btn-block', 'method': 'GET'})
