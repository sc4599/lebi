# coding=utf-8
from application.extensions.database import db


class Groups(db.Document):
    name = db.StringField()
