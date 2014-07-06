#!/usr/bin/env python
from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app as app

acct_app = Blueprint('acct', __name__)


@acct_app.route('/')
def login():
    return render_template('acct/login.html')

@acct_app.route('/', methods=['POST'])
def login_post():
    username = request.form.get('txtName')
    password = request.form.get('txtPwd')

    if username == '' or password == '':
        flash('Fields required', 'error')
        return redirect(url_for('.login'))

    user = app.db.users.find_one({'user_name': username})

    if user:
        session['username'] = user['user_name']
        flash('Login successful')
        return redirect(url_for('main.index', user_id=user['user_id']))
    else:
        flash('Access Denied')
        return redirect(url_for('.login'))


@acct_app.route('/register')
def register():
    return render_template('acct/register.html')

@acct_app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('txtName')
    password = request.form.get('txtPwd')

    if username == '' or password == '':
        flash('Fields required', 'error')
    else:
        # 1. check if user already exists
        user_cnt = app.db.users.find({'user_name': username}).count()
        if user_cnt > 0:
            flash('Username already exists.')
        else:
            # 2. get the next 'user_id'
            max_id = app.db.users.find_one(sort=[('user_id', -1)])
            new_user_id = max_id['user_id'] + 1

            # 3. insert new user
            app.db.users.insert({'user_id': new_user_id, 'user_name': username, 'age': 35})
            flash('Done creating new user')

    return redirect(url_for('.register'))