# coding=utf-8
from datetime import datetime
from application.extensions.database import db


class LeBi(db.Document):
    send_to = db.ObjectIdField()
    reason = db.StringField()
    effect = db.StringField()  # 成果
    creator = db.ObjectIdField()
    created_at = db.DateTimeField(default=datetime.now)
    sender_group_id = db.ObjectIdField()
    creator_group_id = db.ObjectIdField()
