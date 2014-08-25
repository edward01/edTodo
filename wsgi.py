#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, request
from acct import acct_app
from main import main_app
from todo import todo_app
from config import db_config
import pymongo_safe

app = Flask('edTodo')
app.config.from_object('config')

app.register_blueprint(acct_app)
app.register_blueprint(main_app)
app.register_blueprint(todo_app)
# app.register_blueprint(acct_app, url_prefix='/acct') # --to test

# database initialization
conn = pymongo_safe.MongoHandler(db_config)
app.db = conn['test'].test


@app.before_request
def before_request():
    print request


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return redirect(url_for('acct.login'))


if __name__ == '__main__':
    app.run(debug=True)


# todo:
# 1. flash msg
# 2. bootstrap
# 3. database