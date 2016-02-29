# coding=utf-8
from datetime import datetime
from application.extensions.database import db
from werkzeug.security import generate_password_hash


class Admins(db.Document):
    username = db.StringField()
    password = db.StringField()
    created_at = db.DateTimeField(default=datetime.now)

    @classmethod
    def create(cls, username, password):
        admin = Admins()
        admin.username = username
        admin.password = generate_password_hash(password)
        admin.save()
        return admin
