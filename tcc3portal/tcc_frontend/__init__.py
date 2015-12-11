# coding:utf-8
"""
    tcc3portal.tcc_frontend
    ~~~~~~~~~~~~~~~~~~~

    tcc3portal tcc_frontend ui templates package.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""

from flask import Blueprint, Flask, url_for, current_app


def tcc_frontend_find_resource(filename, cdn, local=True):
    """Resource finding function, also available in templates."""
    cdns = current_app.extensions['tcc_frontend']['cdns']
    resource_url = cdns[cdn].get_resource_url(filename)
    return resource_url


def get_app_config(variable_name):
    try:
        return current_app.config[variable_name]
    except KeyError:
        return None


class StaticCDN(object):
    """A CDN that serves content from the local application.

    :param static_endpoint: Endpoint to use.
    """
    def __init__(self, static_endpoint='static'):
        self.static_endpoint = static_endpoint

    def get_resource_url(self, filename):
        extra_args = {}

        return url_for(self.static_endpoint, filename=filename, **extra_args)


class TccFrontend(object):
    def __init__(self, app):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """ Init Flask app.
        :type app: Flask
        """
        blueprint = Blueprint('tcc_frontend',
                              __name__,
                              static_folder="static",
                              template_folder="templates",
                              static_url_path=app.static_url_path+'/tcc_frontend')
        app.register_blueprint(blueprint)

        app.jinja_env.globals['tcc_frontend_find_resource'] =\
            tcc_frontend_find_resource

        local = StaticCDN('tcc_frontend.static')
        static = StaticCDN()

        app.extensions['tcc_frontend'] = {
            'cdns': {
                'local': local,
                'static': static,
            },
        }

        app.jinja_env.globals['get_app_config'] = get_app_config
