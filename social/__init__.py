import os
from flask import Flask
import neomodel
from .models import LastName
from .models import User


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    with app.open_resource('.db_cred') as f:
        db_cred = f.read().decode('utf8')

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=db_cred,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from social.views.hello_test import hello_test
    app.register_blueprint(hello_test)

    from . import db
    db.init_app(app)
    neomodel.db.set_connection(
        url=app.config["DATABASE"]
    )


    return app
