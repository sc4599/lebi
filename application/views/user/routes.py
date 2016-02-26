# coding=utf-8
from flask import Blueprint, render_template


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
def index():
    return render_template('user/index.html')


@user_blueprint.route('/')
def send_lebi():
    return render_template('user/send_lebi.html')
