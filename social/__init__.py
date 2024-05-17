import os
from datetime import date

from flask import Flask
import neomodel


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    db_cred = ""

    with app.open_resource('.db_cred') as f:
        db_cred = f.read().decode('utf8')

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=db_cred,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        db.get_db()
        with neomodel.db.transaction:
            goszti_name = db.LastName(last_name='Goszti', name_day=date.fromisoformat('1992-04-12')).save()
            goszti = db.User(first_name='Kovacs', email='valami@valami.com').save()
            goszti.last_name.connect(goszti_name)
            goszti.save()


        # goszti.last_name.connect(goszti_name)
        # goszti.save()


        return 'Hello, World!'

    from . import db
    db.init_app(app)

    return app
