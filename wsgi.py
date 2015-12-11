# coding:utf-8
"""
    wsgi
    ~~~~

    tcc3portal wsgi interface.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""

from werkzeug.wsgi import DispatcherMiddleware

from tcc3portal import api, portal, train, settings_override


application = DispatcherMiddleware(portal.create_app(settings_override=settings_override), {
    '/api': api.create_app(settings_override=settings_override),
    '/train': train.create_app(settings_override=settings_override),
})

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 9000, application, use_reloader=True, use_debugger=True)

