# coding:utf-8

"""
    tcc3portal.models
    ~~~~~~~~~~~~~~~~~

    tcc3portal db models.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
import sys
import datetime
from flask_login import UserMixin, AnonymousUserMixin
from flask_mongoengine import MongoEngine

db = MongoEngine()

if sys.version >= '3':
    unicode = str

__all__ = ['UserProfile', 'AnonymousUser', 'db', 'GENDER_LIST']

GENDER_LIST = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown')
]


class UserProfile(db.Document, UserMixin):
    """User profile information."""
    meta = {'collection': 'user_profile'}

    nick_name = db.StringField(required=True, max_length=24)
    email = db.EmailField(required=True)

    real_name = db.StringField(max_length=24)
    # phones = db.ListField(db.ReferenceField(UserPhone, reverse_delete_rule=NULLIFY))
    birth = db.DateTimeField(default=datetime.datetime.now())
    gender = db.StringField(max_length=3, choices=GENDER_LIST, default=GENDER_LIST[2])
    brief_description = db.StringField(max_length=140)

    # is_active = db.BooleanField(required=True, default=True)
    # is_authenticated = db.BooleanField(required=True, default=True)

    def __str__(self):
        return unicode(self.nick_name)

    def get_id(self):
        return unicode(self.id)


class AnonymousUser(AnonymousUserMixin):

    nick_name = 'AnonymousUser'

    def __str__(self):
        return unicode(self.nick_name)

    def get_id(self):
        return None
