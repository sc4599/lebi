# coding=utf-8
from application import create_app
from flask.ext.script import Manager
from application.models.admin import Admins
from application.models.groups import Groups
from application.models.user import Users


app = create_app('config.cfg')
manager = Manager(app)


@manager.command
def create_admin(username, password):
    Admins.create(username, password)
    print 'Admin created! username is {username}, password is {password}'.format(**{
        'username': username,
        'password': password,
    })


@manager.command
def init_group():
    groups = [u'总裁办', u'人力资源', u'产品中心', u'交付中心', u'技术支持值班', u'客户服务部', u'技术实验室', u'营销中心', u'红包游戏工作室', u'电玩工作室', u'宝石风暴工作室', u'易搜项目', u'牵手项目组', u'兑兑网游']
    for g in groups:
        Groups.create(g)


@manager.command
def init_users():
    users = []
    with open('data.csv', 'r') as f:
        text = f.read().split('\n')
    for item in text:
        if not item:
            continue
        item = item.split(',')
        users.append({
            'name': item[0].decode('utf-8'),
            'group': item[1].decode('utf-8'),
            'gender': item[2].decode('utf-8'),
        })
        f.close()

    for user in users:
        group = Groups.objects(name=user['group']).first()

        Users.create(
            username=user['name'],
            group_id=group.id,
            gender=Users.GENDER[{u'男': 'male', u'女': 'female'}[user['gender']]],
            password=app.config.get('DEFAULT_PASSWORD'),
        )


if __name__ == '__main__':
    manager.run()
