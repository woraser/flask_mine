#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, json, session, redirect, url_for, request
from . import main
import psutil

@main.before_app_request
def before_request():
    if str(request.url_rule) != '/auth/login' and session.get('is_login') is None:
        return redirect(url_for('auth.login'))

@main.after_app_request
def after_request(response):
    return response

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/index', methods=['GET', 'POST'])
def default():
    return render_template('index.html')

@main.route('/systemInfo', methods=['GET'])
def getSystemInfo():
    response = {
        "cpu_usage": psutil.cpu_percent(0),
        "ram_usage": psutil.virtual_memory().percent
    }
    return json.dumps(response)