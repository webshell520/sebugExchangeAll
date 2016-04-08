#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Neargle -- Neargle.com

import requests
import os

# Reads the configuration file conf.ini and set the configuration
if os.path.exists('conf.ini'):
    print('Importing environment from conf.ini...')
    for line in open('conf.ini'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]


poc_payload = {
    "type":"poc",
    "anonymous":'true'
}

detail_payload = {
    "type":"detail",
    "anonymous": 'true'
}


headers = {
    'Host': 'www.seebug.org',
    'Connection': 'keep-alive',
    'Content-Length': '34',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://www.seebug.org',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'X-CSRFToken': '4AGR8HtjYGKX8kXkdaf0BQsQ3159eqMg',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://www.seebug.org/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2'
}


params = {
    'sessionKey': os.environ.get('sessionKey'),
    'csrftoken': os.environ.get('csrftoken')
}

def exchange(ssvid=0):
    url = 'https://www.seebug.org/vuldb/ssvid-' + str(ssvid)
    poc_r = requests.post(
        url, params=params, headers=headers,
        data=poc_payload, verify=False
    )
    detail_r = requests.post(
        url, params=params, headers=headers,
        data=detail_payload, verify=False
    )
    print poc_r.content
    print detail_r.content


if __name__ == '__main__':
    exchange(15229)
