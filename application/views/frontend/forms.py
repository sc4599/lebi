# coding=utf-8
from flask.ext.wtf import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(Form):
    username = StringField(u'用户名', [DataRequired(u'用户名不能为空')])
    password = PasswordField(u'密码', [DataRequired(u'用户名不能为空')])
    password2 = PasswordField(u'确认密码', [EqualTo('password', u'两次输入的密码不一致!')])

