# #!/usr/bin/env python
# from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app as app
#
# acct_app = Blueprint('acct', __name__, url_prefix='/acct')
#
#
# @acct_app.route('/login')
# def login():
#     return render_template('acct/login.html')
#
# @acct_app.route('/login', methods=['POST'])
# def login_post():
#     username = request.form.get('txtName')
#     password = request.form.get('txtPwd')
#
#     if username is None or password is None:
#         flash('Fields required', 'error')
#         return redirect(url_for('.login'))
#
#     user = app.db.users.find_one({'user_name': username})
#
#     if user:
#         flash('Login successful')
#         session['username'] = user['user_name']
#         return redirect(url_for('main.index'))
#     else:
#         flash('Access Denied')
#         return redirect(url_for('.login'))
#
#
# @acct_app.route('/register')
# def register():
#     return render_template('acct/register.html', error=request.method)
#
# @acct_app.route('/register', methods=['POST'])
# def register_post():
#     username = request.form.get('txtName')
#     password = request.form.get('txtPwd')
#
#     if username is None or password is None:
#         flash('Fields required', 'error')
#     else:
#         flash('Save successful')
#
#     return redirect(url_for('.register'))