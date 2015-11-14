# coding:utf-8
"""
    tcc3portal.api.list
    ~~~~~~~~~~~~~~~~~~~

    tcc3portal api list module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import Blueprint, url_for, render_template

from .helpers import init_api

bp = Blueprint('list', __name__)


@bp.route('/')
def api_list():
    apis = [
        {'part': 'List',
         'url': url_for('list.api_list'),
         'details': 'show all apis.',
         'params': {},
         },
        {'part': 'User',
         'url': url_for('users.show_list'),
         'details': 'show all users.',
         'params': {},
         },
        {'part': 'User',
         'url': url_for('users.show_user', user_name=''),
         'details': 'show a single user what you wanna.',
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
