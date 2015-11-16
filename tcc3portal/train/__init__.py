# coding:utf-8
"""
    tcc3portal.train
    ~~~~~~~~~~~~~~~~

    tcc3portal train data analytics application package.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import render_template
# from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from . import settings as default_settings
from ..tcc_core import factory
# from ..core import nav
#
# nav.register_element('nav_top', Navbar(
#     View('TCC3 Portal', 'dashboard.index'),
#     View('Home', 'dashboard.index'),
#     Link('Api', 'api'),
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


def create_app(settings_override=default_settings or None):
    """Returns the Tcc3Portal dashboard application instance"""
    app = factory.create_app(__name__, __path__, settings_override)

    # if not app.debug:
    for e in [500, 404]:
        app.errorhandler(e)(handle_error)

    return app


def handle_error(e):
    return render_template('errors/%s.html' % e.code), e.code

