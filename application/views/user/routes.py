# coding=utf-8
from flask import Blueprint, render_template, current_app
from .forms import SendLebiForm
from flask.ext.login import login_required, current_user
from application.models.lebi import LeBi


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
@login_required
def index():
    result = LeBi.objects().all()
    return render_template('user/index.html', result=result)


@user_blueprint.route('/send/lebi/', methods=['GET', 'POST'])
@login_required
def send_lebi():
    if current_user.current_month_sent_count >= current_app.config.get('MONTH_LEBI_NUM', 10):
        form = None
        return render_template('user/send_lebi.html', form=form)
    form = SendLebiForm()
    form.init_choices()
    if form.validate_on_submit():
        LeBi.create(
            receiver_id=form.receiver.data,
            reason=form.reason.data,
            effect=form.effect.data,
            creator=current_user,
        )
    return render_template('user/send_lebi.html', form=form)
