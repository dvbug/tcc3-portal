# coding:utf-8
"""
    tcc3portal.train
    ~~~~~~~~~~~~~~~~

    tcc3portal train data analytics application package.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import render_template
from . import settings as default_settings
from ..tcc_core import factory


def create_app(settings_override=None):
    """Returns the Tcc3Portal dashboard application instance"""
    app = factory.create_app(__name__, __path__, default_settings)
    app.config.from_object(settings_override)

    # if not app.debug:
    for e in [500, 404]:
        app.errorhandler(e)(handle_error)

    return app


def handle_error(e):
    return render_template('errors/%s.html' % e.code), e.code

