# coding:utf-8
"""
    tcc3portal.tcc_core.babel
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    tcc3portal tcc_core babel module, based on Flask-Babel.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import Flask, request
from flask_babel import Babel, lazy_gettext, _
from ..settings import LANGUAGES

__all__ = ['TCC3Babel', 'lazy_gettext', '_']


class TCC3Babel(object):
    DEFAULT_LOCALE = 'zh_Hans_CN'

    def __init__(self, app=None):
        self._locale = TCC3Babel.DEFAULT_LOCALE
        self.babel = Babel()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """:type app : Flask"""

        self.babel.init_app(app)
        self.babel.localeselector(TCC3Babel.get_locale)

    def set_locale(self, locale=DEFAULT_LOCALE):
        self._locale = locale
        # TODO

    @classmethod
    def get_locale(cls):
        locale = request.accept_languages.best_match(LANGUAGES.keys())
        print('locale: ', locale)
        return locale
