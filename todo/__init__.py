#!/usr/bin/env python
from flask import Blueprint, render_template, url_for, current_app as app

todo_app = Blueprint('todo', __name__, url_prefix='/todo')


@todo_app.route('/', methods=['GET'])
def index():
    return render_template('todo/index.html')


@todo_app.route('/', methods=['POST'])
def index_post():
    return render_template('todo/index.html')


@todo_app.route('/entry/<todo_id>', methods=['GET'])
def todo_maint():
    return render_template('todo/index.html')


@todo_app.route('/entry/<todo_id>', methods=['POST'])
def todo_maint_post():
    return render_template('todo/index.html')