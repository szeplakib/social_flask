from flask import Blueprint
from datetime import date
from social import db
from social.models import User, LastName
import neomodel

hello_test = Blueprint('hello_test', __name__)

@hello_test.route('/hello')
def hello():
    db.get_db()
    with neomodel.db.transaction:
        goszti_name = LastName(last_name='Goszti', name_day=date.fromisoformat('1992-04-12')).save()
        goszti = User(first_name='Kovacs', email='valami@valami.com').save()
        goszti.last_name.connect(goszti_name)
        goszti.save()

    with neomodel.db.transaction:
        geri_name = LastName(last_name='Geri', name_day=date.fromisoformat('1992-04-12')).save()
        geri = User(first_name='Kovacs', email='valami1@valami.com').save()
        geri.last_name.connect(geri_name)
        geri.save()

    with neomodel.db.transaction:
        goszti = User.nodes.get(email='valami@valami.com')
        geri = User.nodes.get(email='valami1@valami.com')
        goszti.friends.connect(geri)
        goszti.save()
        geri.friends.connect(goszti)
        geri.save()

    return 'Hello, World!'
