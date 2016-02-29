# coding=utf-8
import calendar
from datetime import datetime, date
from application.extensions.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin, current_app
from application.models.groups import Groups


class Users(db.Document, UserMixin):
    GENDER = {
        'male': 1,  # 男
        'female': 0,  # 女
    }

    GENDER_FORMAT = {
        1: u'男',
        0: u'女'
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

    def check_password(self, password):
        if check_password_hash(self.password, password):
            return True

    @property
    def current_month_sent_count(self):
        """
        发送乐币数量
        :return:
        """
        from application.models.lebi import LeBi
        today = date.today()
        end_day = calendar.monthrange(today.year, today.month)[1]
        start_date = today.replace(day=1)
        end_date = today.replace(day=end_day)
        return LeBi.objects(
            creator_id=self.id,
            created_at__gte=start_date,
            created_at__lt=end_date,
        ).count()

    @property
    def created_time(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    @property
    def group(self):
        return Groups.objects(id=self.group_id).first()

    @property
    def serialize(self):
        return {
            'id': str(self.id),
            'username': self.username,
            'gender': self.GENDER_FORMAT[self.gender],
            'created_time': self.created_time,
            'group_name': self.group.name,
            'qq_num': self.qq_num,
            'email': self.email,
        }

    @property
    def using_default_password(self):
        return check_password_hash(self.password, current_app.config.get('DEFAULT_PASSWORD'))

    def set_password(self, password):
        self.password = generate_password_hash(password)
        self.save()
