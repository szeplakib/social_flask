from flask import render_template, redirect, url_for, request, Blueprint, current_app
from social.views.auth import login_required
from social.forms import SearchForm
from social.models import User


index = Blueprint('index', __name__)

@index.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm(request.args)
    users = None
    if form.search.data and request.method == 'GET':
        search_word = f'.*{form.search.data}.*\\@.*\\..*'
        users = User.nodes.filter(email__regex=search_word)
    return render_template(
        'index/search.html',
        form=form,
        entities=[user.email for user in users]
    )