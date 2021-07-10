#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hello@yeshen.org'

import subprocess,os,os.path
from bottle import route, run, template, run, post, request, response, get

@route('/')
def index():
    return html_rtc()

@route('/rtc/')
def html_rtc():
    data = ''
    with open('index.html', 'r') as f:
        data = f.read()
    return data


@get('/rtc/<id>/<type>')
def get_rtc(id,type):
    target = getName(id,type)
    data = ''
    if not os.path.exists(target):
        print 'not found, skipping:' + target
        return data
    with open(target, 'r') as f:
        data = f.read()
    os.remove(target)
    print 'found:' + target
    return data


@post('/rtc/<id>/<type>')
def post_rtc(id,type):
    target = getName(id,type)
    if os.path.exists(target):
        os.remove(target)
    print request.json
    data = request.json['content']
    with open(target, 'w') as f:
        f.write(data)
    print 'wrote:' + target
    return "done"


def getName(id,type):
    return 'data/data' + id + type


if not os.path.exists('data'):
    os.makedirs('data')
run(host='127.0.0.1', port=2021)
