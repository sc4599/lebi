# coding=utf-8
from flask import Blueprint, jsonify, request
from flask.ext.login import login_required, current_user
from application.models.user import Users


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/')
@login_required
def index():
    return jsonify({
        'data': 'api route',
        'status': True,
    })


@api_blueprint.route('/group/users/')
@login_required
def group_users():
    group_id = request.args.get('group_id')
    if not group_id:
        return jsonify({
            'status': False,
            'reason': u'缺少 group_id 参数',
        })

    data = Users.objects(group_id=group_id).all()
    ret = []
    for item in data:
        item = item.serialize
        if item['username'] != current_user.username:
            ret.append({'username': item['username'], 'id': item['id']})
    return jsonify({
        'status': True,
        'data': ret,
    })
