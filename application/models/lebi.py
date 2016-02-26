# coding=utf-8
from datetime import datetime
from application.extensions.database import db
from application.models.user import Users


class LeBi(db.Document):
    receiver_id = db.ObjectIdField()  # 接受人
    reason = db.StringField()
    effect = db.StringField()  # 成果
    creator_id = db.ObjectIdField()
    created_at = db.DateTimeField(default=datetime.now)
    receiver_group_id = db.ObjectIdField()
    creator_group_id = db.ObjectIdField()

    @classmethod
    def create(cls, receiver_id, reason, effect, creator):
        receiver = Users.objects(id=receiver_id).first()
        lebi = LeBi(
            receiver_id=receiver.id,
            reason=reason,
            effect=effect,
            creator_id=creator.id,
            receiver_group_id=receiver.group_id,
            creator_group_id=creator.group_id,
        )
        lebi.save()
        return lebi

    @property
    def receiver(self):
        return Users.objects(id=self.receiver_id).first()

    @property
    def creator(self):
        return Users.objects(id=self.creator_id).first()

    @property
    def format(self):
        return u'{creator}发给{receiver}'.format(creator=self.creator.username, receiver=self.receiver.username)

    @property
    def created_time(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
