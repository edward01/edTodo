#!/usr/bin/env python
from flask import Blueprint, render_template, session, current_app as app

main_app = Blueprint('main', __name__, url_prefix='/main')


@main_app.route('/<user_id>')
def index(user_id):
    print 'index'
    user = app.db.users.find_one({'user_name': session['username']})
    return render_template('main/main.html', user=user['user_name'], user_id=user_id)