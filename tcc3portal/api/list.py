# coding:utf-8
"""
    tcc3portal.api.list
    ~~~~~~~~~~~~~~~~~~~

    tcc3portal api list module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import Blueprint, url_for, render_template
from ..tcc_core.babel import _
from .helpers import init_api

bp = Blueprint('list', __name__)


@bp.route('/')
def api_list():
    apis = [
        {'part': _('List'),
         'url': url_for('list.api_list'),
         'details': _('show all apis.'),
         'params': {},
         },
        {'part': _('User'),
         'url': url_for('users.show_list'),
         'details': _('show all users.'),
         'params': {},
         },
        {'part': _('User'),
         'url': url_for('users.show_user', user_name=''),
         'details': _('show a single user what you wanna.'),
         'params': [
                {
                    'name': 'user_name',
                    'type': 'string',
                }
            ],
         },
    ]
    apis = [init_api(api) for api in apis]
    return render_template('api_list.html', apis=apis)
