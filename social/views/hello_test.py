from flask import Blueprint, current_app
from datetime import date
from social import db
from social.models import User
import neomodel
from flask_bcrypt import Bcrypt

hello_test = Blueprint('hello_test', __name__)

@hello_test.route('/hello')
def hello():
    bcrypt = Bcrypt(current_app)
    db.get_db()
    with neomodel.db.transaction:
        # goszti_name = LastName(
        #     last_name='Goszti',
        #     name_day=date.fromisoformat('1992-04-12')
        # ).save()
        goszti = User(
            first_name='Kovacs',
            email='valami@valami.com',
            password=bcrypt.generate_password_hash('valami').decode('utf-8')
        ).save()
        # goszti.last_name.connect(goszti_name)
        goszti.save()

    with neomodel.db.transaction:
        # geri_name = LastName(
        #     last_name='Geri',
        #     name_day=date.fromisoformat('1992-04-12')
        # ).save()
        geri = User(
            first_name='Kovacs',
            email='valami1@valami.com',
            password=bcrypt.generate_password_hash('valami2').decode('utf-8')
        ).save()
        # geri.last_name.connect(geri_name)
        geri.save()

    with neomodel.db.transaction:
        goszti = User.nodes.get(email='valami@valami.com')
        geri = User.nodes.get(email='valami1@valami.com')
        goszti.friends.connect(geri)
        goszti.save()
        geri.friends.connect(goszti)
        geri.save()

    result = ""
    goszti = User.nodes.get(email='valami@valami.com')
    geri = User.nodes.get(email='valami1@valami.com')
    if (
        bcrypt.check_password_hash(goszti.password, 'valami') and
            bcrypt.check_password_hash(geri.password, 'valami2')
    ):
        result = "siker"
    else:
        result = "kudarc"

    return result
