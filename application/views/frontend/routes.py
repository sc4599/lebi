# coding=utf-8
from flask import Blueprint, render_template, url_for, redirect
from forms import RegisterForm, LoginForm
from flask.ext.login import login_user, logout_user


frontend_blueprint = Blueprint('frontend', __name__)


@frontend_blueprint.route('/')
def index():
    return render_template('frontend/index.html')


@frontend_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template('frontend/register.html', form=form)


@frontend_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        return redirect(url_for('user.index'))
    return render_template('frontend/login.html', form=form)


@frontend_blueprint.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('frontend.index'))
