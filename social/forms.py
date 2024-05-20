from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, Optional


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        [DataRequired()],
        render_kw={'class': 'form-control'}
    )
    password = PasswordField(
        'Password',
        [DataRequired()],
        render_kw={'class': 'form-control'}
    )
    submit = SubmitField('Login', render_kw={'class': 'btn btn-success btn-block'})


class RegisterForm(FlaskForm):
    email = StringField(
        'Email',
        [DataRequired()],
        render_kw = {'class': 'form-control'}
    )
    password = PasswordField(
        'Password',
        [Length(min=3)],
        render_kw={'class': 'form-control'}
    )
    first_name = StringField(
        'First Name',
        render_kw={'class': 'form-control'}
    )
    last_name = StringField(
        'Last Name',
        render_kw={'class': 'form-control'}
    )
    birthday = DateField(
        'Birthday',
        [Optional()],
        render_kw={'class': 'form-control'}
    )
    submit = SubmitField('Resister', render_kw={'class': 'btn btn-success btn-block'})


class SearchForm(FlaskForm):
    search = StringField(
        'search',
        [DataRequired()],
        render_kw={
            'class': 'form-control',
            'type': 'search',
            'placeholder': 'User email',
            'aria-label': 'Search'
        }
    )
    submit = SubmitField(
        'Search',
        render_kw={'class': 'btn btn-dark'}
    )
