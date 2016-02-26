# coding=utf-8
from flask.ext.wtf import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from application.models.user import Users


class RegisterForm(Form):
    username = StringField(u'用户名', [DataRequired(u'用户名不能为空')])
    password = PasswordField(u'密码', [DataRequired(u'用户名不能为空')])
    password2 = PasswordField(u'确认密码', [EqualTo('password', u'两次输入的密码不一致!')])


class LoginForm(Form):
    username = StringField(u'用户名', [DataRequired(u'用户名不能为空')])
    password = PasswordField(u'密码', [DataRequired(u'用户名不能为空')])

    def validate_username(self, field):
        if not self.user:
            raise ValidationError(u'用户名 {username} 不存在！'.format(username=field.data))

    def validate_password(self, field):
        if not self.user.check_password(field.data):
            raise ValidationError(u'密码错误')

    @property
    def user(self):
        return Users.objects(username=self.username.data).first()

