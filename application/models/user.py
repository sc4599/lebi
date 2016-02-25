# coding=utf-8
from datetime import datetime
from application.extensions.database import db


class Users(db.Document):
    username = db.StringField()
    password = db.StringField()
    gender = db.IntField()
    created_at = db.DateTimeField(default=datetime.now)
    group_id = db.ObjectIdField()
    qq_num = db.StringField()
    email = db.StringField()
