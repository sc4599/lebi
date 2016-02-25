# coding=utf-8
from flask import Blueprint, render_template
from forms import RegisterForm


frontend_blueprint = Blueprint('frontend', __name__)


@frontend_blueprint.route('/')
def index():
    return render_template('frontend/index.html')


@frontend_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template('frontend/register.html')
