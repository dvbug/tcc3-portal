# coding:utf-8
"""
    run
    ~~~~

    tcc3portal run test module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""

from werkzeug.wsgi import DispatcherMiddleware
from tcc3portal import api, portal, train

application = DispatcherMiddleware(portal.create_app(), {
    '/api': api.create_app(),
    '/train': train.create_app(),
})

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 9000, application, use_reloader=True, use_debugger=True)
