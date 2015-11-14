# coding:utf-8
"""
    tcc3portal.api.helpers
    ~~~~~~~~~~~~~~~~~~~~~~

    helper module.
"""


def split_api(api_url):
    """Returns sub api url without /api/."""
    return '/'.join(api_url.lstrip('/').split('/')[1:]) or '/api'


def init_api(api: dict):
    api['short_url'] = split_api(api['url'])
    return api
