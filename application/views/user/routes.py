# coding=utf-8
from flask import Blueprint, render_template, current_app, redirect, url_for
from .forms import SendLebiForm, PasswordEditForm
from flask.ext.login import login_required, current_user
from application.models.lebi import LeBi


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
@login_required
def index():
    result = LeBi.objects().all()
    return render_template('user/index.html', result=result)


@user_blueprint.route('/send/lebi/', methods=['GET', 'POST'])
@user_blueprint.route('/send/lebi/<string:oid>/')
@login_required
def send_lebi(oid=None):
    if current_user.current_month_sent_count >= current_app.config.get('MONTH_LEBI_NUM', 10):
        form = None
        return render_template('user/send_lebi.html', form=form)
    if oid:
        obj = LeBi.objects(id=oid).first()
        form = SendLebiForm(obj=obj)
    else:
        form = SendLebiForm()
    form.init_choices()
    if form.validate_on_submit():
        LeBi.create(
            receiver_id=form.receiver_id.data,
            reason=form.reason.data,
            effect=form.effect.data,
            creator=current_user,
        )
        return redirect(url_for('user.index'))
    return render_template('user/send_lebi.html', form=form)


@user_blueprint.route('/password/edit/', methods=['GET', 'POST'])
@login_required
def password_edit():
    form = PasswordEditForm()
    if form.validate_on_submit():
        current_user.set_password(form.new_password.data)
        return redirect(url_for('user.index'))
    return render_template('user/password_edit.html', form=form)
