# coding=utf-8
from flask import Blueprint, render_template
from .forms import SendLebiForm
from flask.ext.login import login_required


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
@login_required
def index():
    return render_template('user/index.html')


@user_blueprint.route('/send/lebi/', methods=['GET', 'POST'])
def send_lebi():
    form = SendLebiForm()
    form.init_choices()
    if form.validate_on_submit():
        print form.receiver.data
    return render_template('user/send_lebi.html', form=form)
