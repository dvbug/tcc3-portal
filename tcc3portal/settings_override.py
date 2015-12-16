# coding:utf-8
"""
    settings override
    ~~~~~~~~~~~~~~~~~~~

    settings override
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
DEBUG = True

MONGODB_SETTINGS = {
    'db': 'tccdevdb',
    'host': '192.168.1.118',
    'port': 20000
}

DAC_HOST_URL = 'dac.tcc.org'  # '192.168.1.118:8080'
DAC_API_CONFIGS_LINES_URL = '/api/v1.0/configs/lines'
DAC_API_SCHEDULES_URL = '/api/v1.0/schedules/'


SSO_CENTER_HOST = 'sso.tcc.org'  # '192.168.1.118:9001'
SSO_CENTER_URL = 'http://'+SSO_CENTER_HOST
SSO_CENTER_REGISTER_URL = 'http://'+SSO_CENTER_HOST+'/sso/register'
SSO_CENTER_REFERRER_KEY = 'url'
SSO_CENTER_LOGOUT_URL = 'http://'+SSO_CENTER_HOST+'/sso/logout'
SSO_CENTER_API_TICKET_CHECK_ENDPOINT = '/api/validation'

