# coding=utf-8
from application.extensions.database import db


class Groups(db.Document):
    name = db.StringField()

    @classmethod
    def create(cls, name):
        group = Groups(name=name)
        group.save()
        return group
