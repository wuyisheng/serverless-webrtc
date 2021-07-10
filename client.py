#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hello@yeshen.org'

import requests

request_path = 'http://localhost:2021/rtc/12653/answer'
response = requests.post(request_path,json={"content": "value"})
print response.text

response = requests.get(request_path)
print response.text
