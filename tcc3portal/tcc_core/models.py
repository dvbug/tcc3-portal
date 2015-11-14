# coding:utf-8

"""
    tcc3portal.models
    ~~~~~~~~~~~~~~~~~

    tcc3portal db models.
"""
import sys
from flask_login import UserMixin, AnonymousUserMixin
from flask_mongoengine import MongoEngine

db = MongoEngine()

if sys.version >= '3':
    unicode = str

__all__ = ['User', 'AnonymousUser', 'db']


class User(db.Document, UserMixin):

    name = db.StringField(required=True, max_length=64)
    password = db.StringField(max_length=256)
    email = db.StringField(max_length=64)
    description = db.StringField(max_length=1024)

    def __str__(self):
        return unicode(self.name)

    def get_id(self):
        return unicode(self.id)


class AnonymousUser(AnonymousUserMixin):

    name = 'AnonymousUser'

    def __str__(self):
        return unicode(self.name)

    def get_id(self):
        return None
