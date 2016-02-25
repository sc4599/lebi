# coding=utf-8
from flask import Blueprint, render_template


frontend_blueprint = Blueprint('frontend', __name__)


@frontend_blueprint.route('/')
def index():
    return render_template('frontend/index.html')
