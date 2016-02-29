# coding=utf-8
from flask import Blueprint, render_template, current_app, redirect, url_for, request, abort
from .forms import SendLebiForm, PasswordEditForm
from flask.ext.login import login_required, current_user
from application.models.lebi import LeBi


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
@login_required
def index():
    count = {
        'received_count': LeBi.objects(receiver_id=current_user.id).count(),
        'created_count': LeBi.objects(creator_id=current_user.id).count(),
    }
    return render_template('user/index.html', count=count)


@user_blueprint.route('/records/')
@user_blueprint.route('/records/<string:act>/')
@login_required
def records(act=None):
    page = request.args.get('page', 1)
    page = int(page)
    if act == 'received':
        result = LeBi.objects(receiver_id=current_user.id).paginate(page=page, per_page=20)
    elif act == 'created':
        result = LeBi.objects(creator_id=current_user.id).paginate(page=page, per_page=20)
    else:
        result = LeBi.objects().order_by('-created_at').paginate(page=page, per_page=20)
    return render_template('user/records.html', result=result, act=act)


@user_blueprint.route('/send/lebi/', methods=['GET', 'POST'])
@user_blueprint.route('/send/lebi/<string:oid>/', methods=['GET', 'POST'])
@login_required
def send_lebi(oid=None):
    if current_user.current_month_sent_count >= current_app.config.get('MONTH_LEBI_NUM', 10):
        form = None
        return render_template('user/send_lebi.html', form=form)
    obj = None
    if oid:
        obj = LeBi.objects(id=oid).first()
        if obj.creator_id != current_user.id:
            abort(403)
        form = SendLebiForm(obj=obj)
    else:
        form = SendLebiForm()
    form.init_choices()
    if form.validate_on_submit():
        if obj:
            obj.receiver_id = form.receiver_id.data
            obj.reason = form.reason.data
            obj.effect = form.effect.data
            obj.receiver_group_id = form.receiver_group_id.data
            obj.save()
        else:
            LeBi.create(
                receiver_id=form.receiver_id.data,
                reason=form.reason.data,
                effect=form.effect.data,
                creator=current_user,
            )
        return redirect(url_for('user.records'))
    return render_template('user/send_lebi.html', form=form)


@user_blueprint.route('/password/edit/', methods=['GET', 'POST'])
@login_required
def password_edit():
    form = PasswordEditForm()
    if form.validate_on_submit():
        current_user.set_password(form.new_password.data)
        return redirect(url_for('user.index'))
    return render_template('user/password_edit.html', form=form)
