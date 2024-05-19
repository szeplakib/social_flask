import functools

from flask import Blueprint, current_app, request, render_template, redirect, url_for, flash, session, g
from social.db import get_db
from social.forms import RegisterForm
from social.models import User
from flask_bcrypt import Bcrypt
import neomodel

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    bcrypt = Bcrypt(current_app)
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        get_db()
        try:
            with neomodel.db.transaction:
                user = User(
                    email=email,
                    password=password,
                    first_name=form.first_name.data,
                    birthday=form.birthday.data
                )
                user.save()
        except neomodel.exceptions.UniqueProperty:
            flash(f"User with email: {email} is already registered.")
        else:
            return redirect(url_for("auth.login"))


    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    bcrypt = Bcrypt(current_app)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        get_db()
        error = None
        try:
            user = User.nodes.get(email=email)
        except neomodel.sync_.core.DoesNotExist:
            user = None

        if user is None:
            error = 'Incorrect username.'
        elif not bcrypt.check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_email'] = user.email
            # return redirect(url_for('index'))
            return redirect(url_for("index.search"))

        flash(error)

    return render_template('auth/login.html')


@auth.before_app_request
def load_logged_in_user():
    user_email = session.get('user_email')

    if user_email is None:
        g.user = None
    else:
        get_db()
        g.user = User.nodes.get(email=user_email)


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
