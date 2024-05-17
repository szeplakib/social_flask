import click
from flask import current_app, g
import neomodel
# from neomodel import config


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


def init_db():
    db = get_db()

    # with current_app.open_resource('schema.sql') as f:
    #     db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


class LastName(neomodel.StructuredNode):
    last_name = neomodel.StringProperty(required=True)
    name_day = neomodel.DateProperty()


class User(neomodel.StructuredNode):
    # uid = UniqueIdProperty()
    email = neomodel.EmailProperty(required=True)
    first_name = neomodel.StringProperty()
    last_name = neomodel.Relationship(LastName, 'HAS_NAME')
    friends = neomodel.Relationship('User', 'ARE_FRIENDS')

