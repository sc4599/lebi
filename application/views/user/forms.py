# coding=utf-8
from flask.ext.wtf import Form
from wtforms.fields import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length
from application.models.user import Users
from application.models.groups import Groups
from flask.ext.login import current_user


class MySelectField(SelectField):
    def pre_validate(self, form):
        pass


class SendLebiForm(Form):
    receiver_id = MySelectField(u'接受人', coerce=str)
    receiver_group_id = SelectField(u'项目组', coerce=str)
    reason = StringField(u'原因', [DataRequired(u'原因不能为空')])
    effect = StringField(u'成果', [DataRequired(u'成果不能为空')])

    def init_choices(self):
        # TODO 此处应该增加发放限制条件
        groups = []
        all_groups = Groups.objects().all()

        for group in all_groups:
            if Users.objects(group_id=group.id).count() > 0:
                if str(group.id) == self.receiver_group_id.data:
                    groups.insert(0, group)
                else:
                    groups.append(group)

        users = Users.objects(group_id=groups[0].id).all()
        self.receiver_id.choices = [
            (str(user.id), user.username) for user in users if user.username != current_user.username
        ]
        self.receiver_group_id.choices = [(str(group.id), group.name) for group in groups]


class PasswordEditForm(Form):
    password = PasswordField(u'原始密码', [DataRequired(u'原始密码不能为空')])
    new_password = PasswordField(u'新密码', [DataRequired(u'新密码不能为空'), Length(min=6, message=u'密码最少6位')])
    new_password2 = PasswordField(u'确认密码', [EqualTo('new_password', u'两次输入的密码不一致')])

    def validate_password(self, field):
        if not current_user.check_password(field.data):
            raise ValidationError(u'原密码不正确！')

        if field.data == self.password.data:
            raise ValidationError(u'新密码不能与原密码一致')
