# coding:utf-8
"""
    tcc3portal.tcc_core.factory
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    tcc3portal tcc_core factory module.
"""
from flask import Flask

from . import db, bootstrap, lm, babel, sso_client
from .helpers import register_blueprints, JSONEncoder
from .middleware import HTTPMethodOverrideMiddleware
from ..tcc_frontend import TccFrontend


__all__ = ['create_app']


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the Tcc3Portal platform.

    :param package_name: application package name.
    :param package_path: application package path.
    :param settings_override: a dictionary of settings to override.
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    :return: Flask application instance.
    """
    app = Flask(package_name, instance_relative_config=True)

    app.json_encoder = JSONEncoder
    app.config.from_object("tcc3portal.settings")
    app.config.from_pyfile("settings.cfg", silent=True)
    app.config.from_object(settings_override)

    # something need init
    # security.init_app(app, None, register_blueprint=register_security_blueprint)
    db.init_app(app)
    bootstrap.init_app(app)
    lm.init_app(app)
    babel.init_app(app)
    sso_client.init_app(app, lm)
    TccFrontend(app)

    register_blueprints(app, package_name, package_path)

    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app

