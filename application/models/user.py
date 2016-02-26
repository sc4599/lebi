# coding=utf-8
from datetime import datetime
from application.extensions.database import db
from werkzeug.security import generate_password_hash


class Users(db.Document):
    GENDER = {
        'male': 1,  # 男
        'female': 0,  # 女
    }

    username = db.StringField()
    password = db.StringField()
    gender = db.IntField()
    created_at = db.DateTimeField(default=datetime.now)
    group_id = db.ObjectIdField()
    qq_num = db.StringField()
    email = db.StringField()

    @classmethod
    def create(cls, username, group_id, gender, password, qq_num=None, email=None):
        user = Users()
        user.username = username
        password = generate_password_hash(password)
        user.password = password
        user.gender = gender
        user.group_id = group_id
        if qq_num:
            user.qq_num = qq_num
        if email:
            user.email = email
        user.save()
        return user
