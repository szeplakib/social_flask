import click
from flask import current_app, g
import neomodel
from .models import User


def get_db():
    if 'db' not in g:
        g.db = neomodel.db.set_connection(
            url=current_app.config["DATABASE"]
        )
        # g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close_connection()


def install_labels():
    db = get_db()
    neomodel.install_labels(User)


@click.command('install_labels')
def install_labels_command():
    """Installs labels. This is going to set constrains and indices."""
    install_labels()
    click.echo('All SPECIFIED lables were installed')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(install_labels_command)





