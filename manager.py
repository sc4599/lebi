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
    groups = [u'人力资源', u'牵手项目组', u'总裁办']
    for g in groups:
        Groups.create(g)


@manager.command
def init_users():
    users = [
        {'name': u'陈强胜', 'group': u'牵手项目组', 'gender': 'male'},
        {'name': u'宋超', 'group': u'牵手项目组', 'gender': 'male'},
        {'name': u'李小玲', 'group': u'总裁办', 'gender': 'female'},
    ]
    for user in users:
        group = Groups.objects(name=user['group']).first()

        Users.create(
            username=user['name'],
            group_id=group.id,
            gender=Users.GENDER[user['gender']],
            password=app.config.get('DEFAULT_PASSWORD', 'zyl.bzw'),
        )


if __name__ == '__main__':
    manager.run()
