# coding:utf-8
"""
    tcc3portal.api
    ~~~~~~~~~~~~~~

    tcc3portal api application package.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from functools import wraps

from flask import jsonify
# from flask_security import login_required
# from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from . import settings as default_settings
from ..tcc_core import Tcc3PortalError, Tcc3PortalFormError
from ..tcc_core.helpers import JSONEncoder
from ..tcc_core import factory

# from ..core import nav as apinav
#
# apinav.register_element('api_nav_top', Navbar(
#     Link('TCC3 Portal', '../'),
#     View('Api List', 'list.api_list'),
#     Subgroup('Tech Support',
#              Link('flask', dest='http://dormousehole.readthedocs.org/en/latest/index.html'),
#              Link('flask-wtf', dest='http://docs.jinkan.org/docs/flask-wtf/index.html'),
#              Link('flask-nav', dest='http://pythonhosted.org/flask-nav/'),
#              Link('flask-pymongo', dest='http://flask-pymongo.readthedocs.org/en/latest/'),
#              Link('flask-bootstrap', dest='http://www.pythonhosted.org/Flask-Bootstrap/'),
#              Link('flask-restful', dest='http://www.pythondoc.com/Flask-RESTful/index.html'),
#              Separator(),
#              Link('mongodb', dest='https://www.mongodb.org/'),
#              )
# ))


def create_app(settings_override=default_settings or None, register_security_blueprint=False):
    """Returns the tcc3portal API application instance"""

    app = factory.create_app(__name__, __path__, settings_override,
                             register_security_blueprint=register_security_blueprint)

    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    # Register custom error handlers
    app.errorhandler(Tcc3PortalError)(on_tcc3portal_error)
    app.errorhandler(Tcc3PortalFormError)(on_tcc3portal_form_error)
    app.errorhandler(404)(on_404)

    return app


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        # @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc
        return f

    return decorator


def on_404(e):
    return jsonify(dict(error='Not found')), 404


def on_tcc3portal_error(e):
    return jsonify(dict(error=e.msg)), 400


def on_tcc3portal_form_error(e):
    return jsonify(dict(errors=e.errors)), 400
