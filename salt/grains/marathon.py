# -*- coding: utf-8 -*-
'''
Generate marathon proxy minion grains.
'''
from __future__ import absolute_import


import salt.utils
import salt.utils.http
__proxyenabled__ = ['marathon']
__virtualname__ = 'marathon'


def __virtual__():
    if not salt.utils.is_proxy() or 'proxy' not in __opts__:
        return False
    else:
        return __virtualname__


def kernel():
    return {'kernel': 'marathon'}


def os():
    return {'os': 'marathon'}


def os_family():
    return {'os_family': 'marathon'}


def os_data():
    return {'os_data': 'marathon'}


def marathon():
    response = salt.utils.http.query(
        "{}/v2/info".format(__opts__['proxy'].get(
            'base_url',
            "http://locahost:8080",
        )),
        decode_type='json',
        decode=True,
    )
    if not response or 'dict' not in response:
        return {'marathon': None}
    return {'marathon': response['dict']}
