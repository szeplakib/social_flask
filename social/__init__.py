import os
from flask import Flask
import neomodel
from .models import User


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from flask_bootstrap import Bootstrap5
    bootstrap = Bootstrap5(app)

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

    from social.views import hello_test, auth, index
    app.register_blueprint(hello_test.hello_test)
    app.register_blueprint(auth.auth)
    app.register_blueprint(index.index)

    from . import db
    db.init_app(app)
    neomodel.db.set_connection(
        url=app.config["DATABASE"]
    )


    return app
