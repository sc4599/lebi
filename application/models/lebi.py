# coding=utf-8
from datetime import datetime
from application.extensions.database import db


class LeBi(db.Document):
    receiver = db.ObjectIdField()  # 接受人
    reason = db.StringField()
    effect = db.StringField()  # 成果
    creator = db.ObjectIdField()
    created_at = db.DateTimeField(default=datetime.now)
    receiver_group_id = db.ObjectIdField()
    creator_group_id = db.ObjectIdField()

    @classmethod
    def create(cls, receiver, reason, effect, creator, sender_group_id, creator_group_id):
        lebi = LeBi(
            receiver=receiver,
            reason=reason,
            effect=effect,
            creator=creator,
            sender_group_id=sender_group_id,
            creator_group_id=creator_group_id,
        )
        lebi.save()
        return lebi
