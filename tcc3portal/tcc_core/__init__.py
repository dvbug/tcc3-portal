# coding:utf-8
"""
    tcc3portal.tcc_core
    ~~~~~~~~~~~~~~~~~~~

    tcc_core package.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from mongoengine.queryset.visitor import Q

from .sso import SSOClient
from .babel import TCC3Babel, lazy_gettext, _
from .models import UserProfile, AnonymousUser, db

__all__ = ['TCC3Babel', 'UserProfile', 'AnonymousUser',
           'bootstrap', 'lm', 'babel', 'sso_client', 'db', 'lazy_gettext', '_',
           'Q', 'Tcc3PortalError', 'Tcc3PortalFormError', ]

bootstrap = Bootstrap()

lm = LoginManager()

babel = TCC3Babel()

sso_client = SSOClient()


class Tcc3PortalError(Exception):
    """Base application error class."""

    def __init__(self, msg):
        self.msg = msg


class Tcc3PortalFormError(Exception):
    """Raise when an error processing a form occurs."""

    def __init__(self, error=None):
        self.error = error
