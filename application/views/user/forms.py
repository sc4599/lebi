# coding=utf-8
from flask.ext.wtf import Form
from wtforms.fields import StringField, SelectField
from wtforms.validators import DataRequired
from application.models.user import Users
from application.models.groups import Groups


class SendLebiForm(Form):
    receiver = SelectField(u'接受人', [DataRequired(u'接受人不能为空!')], coerce=str)
    receiver_group = SelectField(u'项目组', coerce=str)
    reason = StringField(u'原因', [DataRequired(u'原因不能为空')])
    effect = StringField(u'成果', [DataRequired(u'成果不能为空')])

    def init_choices(self):
        groups = []
        all_groups = Groups.objects().order_by().all()
        for group in all_groups:
            if Users.objects(group_id=group.id).count() > 0:
                groups.append(group)

        users = Users.objects(group_id=groups[0].id).all()
        self.receiver.choices = [(str(user.id), user.username) for user in users]
        self.receiver_group.choices = [(str(group.id), group.name) for group in groups]
