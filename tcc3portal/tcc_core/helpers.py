# coding:utf-8
"""
    tcc3portal.tcc_core.helpers
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    tcc3portal tcc_core helpers module.
"""
import pkgutil
import importlib
import urllib.parse
from flask import Blueprint, current_app
from flask.json import JSONEncoder as BaseJSONEncoder
from bson import ObjectId

__all__ = ['register_blueprint', 'register_blueprints',
           'JSONEncoder', 'JsonSerializer', 'get_referrer_name',
           'get_sso_center_url', 'get_sso_center_api_ticket_check_url',
           'get_sso_center_logout_url', 'get_sso_center_register_url'
           ]


def register_blueprint(app, blueprint):
    """
    :type app: flask.Flask
    :type blueprint: flask.Blueprint
    """
    if app is not None:
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)


def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :type app: flask.Flask
    :param app: the Flask application.
    :param package_name: the package name.
    :param package_path: the package path.
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv


class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """
    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(JSONEncoder, self).default(obj)


class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    def to_json(self):
        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        return rv


def get_referrer_name():
    return current_app.config['SSO_CENTER_REFERRER_KEY'] or 'url'


def get_sso_center_url():
    return current_app.config['SSO_CENTER_URL']


def get_sso_center_register_url():
    return current_app.config['SSO_CENTER_REGISTER_URL']


def get_sso_center_logout_url():
    return current_app.config['SSO_CENTER_LOGOUT_URL']


def get_sso_center_api_ticket_check_url():
    sso_center_url = get_sso_center_url()
    sso_center_api_ticket_check_endpoint = current_app.config['SSO_CENTER_API_TICKET_CHECK_ENDPOINT']

    return urllib.parse.urljoin(sso_center_url, sso_center_api_ticket_check_endpoint)