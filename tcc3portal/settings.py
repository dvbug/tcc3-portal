# coding:utf-8
"""
    tcc3portal.settings
    ~~~~~~~~~~~~~~~~~~~

    tcc3portal settings
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
DEBUG = True
SECRET_KEY = "YOU CAN NOT GUESS IT IT IT IT."

# SERVER_NAME = 'tcc3.com'

# PyMongo's setting.
# MONGO_URI = "mongodb://192.168.1.91:20000/tccdevdb"
# MONGO_HOST = "192.168.1.91"
# MONGO_PORT = 20000

MONGODB_SETTINGS = {
    'db': 'tccdevdb',
    'host': '192.168.1.118',
    'port': 20000
}

# MAIL_DEFAULT_SENDER = 'info@overholt.com'
# MAIL_SERVER = 'smtp.postmarkapp.com'
# MAIL_PORT = 25
# MAIL_USE_TLS = True
# MAIL_USERNAME = 'username'
# MAIL_PASSWORD = 'password'
#
SECURITY_POST_LOGIN_VIEW = '/'
SECURITY_PASSWORD_HASH = 'plaintext'
SECURITY_PASSWORD_SALT = 'password_salt'
SECURITY_REMEMBER_SALT = 'remember_salt'
SECURITY_RESET_SALT = 'reset_salt'
SECURITY_RESET_WITHIN = '5 days'
SECURITY_CONFIRM_WITHIN = '5 days'
SECURITY_SEND_REGISTER_EMAIL = False

DAC_HOST_URL = "192.168.1.125:8080"
DAC_API_CONFIGS_LINES_URL = '/api/v1.0/configs/lines'
DAC_API_SCHEDULES_URL = '/api/v1.0/schedules/'


SSO_CENTER_HOST = '192.168.1.125:9001'
SSO_CENTER_URL = 'http://'+SSO_CENTER_HOST
SSO_CENTER_REGISTER_URL = 'http://'+SSO_CENTER_HOST+'/sso/register'
SSO_CENTER_REFERRER_KEY = 'url'
SSO_CENTER_LOGOUT_URL = 'http://'+SSO_CENTER_HOST+'/sso/logout'
SSO_CENTER_API_TICKET_CHECK_ENDPOINT = '/api/validation'


BOOTSTRAP_SERVE_LOCAL = True


SESSION_PROTECTION = "strong"


BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'
LANGUAGES = {
    'zh_Hans_CN': 'Chinese',
    # 'en': 'English',
}
