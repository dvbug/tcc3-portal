# coding:utf-8
"""
    settings override
    ~~~~~~~~~~~~~~~~~~~

    settings override
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
DEBUG = False

MONGODB_SETTINGS = {
    'db': 'tccdevdb',
    'host': '0.0.0.0',
    'port': 20000
}

DAC_HOST_URL = "0.0.0.0:8080"
DAC_API_CONFIGS_LINES_URL = '/api/v1.0/configs/lines'
DAC_API_SCHEDULES_URL = '/api/v1.0/schedules/'


SSO_CENTER_HOST = '0.0.0.0:9001'
SSO_CENTER_URL = 'http://'+SSO_CENTER_HOST
SSO_CENTER_REGISTER_URL = 'http://'+SSO_CENTER_HOST+'/sso/register'
SSO_CENTER_REFERRER_KEY = 'url'
SSO_CENTER_LOGOUT_URL = 'http://'+SSO_CENTER_HOST+'/sso/logout'
SSO_CENTER_API_TICKET_CHECK_ENDPOINT = '/api/validation'

