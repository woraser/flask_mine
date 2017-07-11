#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, json, session, redirect, url_for, request
from flask_login import login_required, current_user
from . import main
import psutil

@main.after_app_request
def after_request(response):
    return response

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@main.route('/index', methods=['GET', 'POST'])
def default():
    return redirect(url_for("main.index"))

@main.route('/base')
@login_required
def baseView():
    return render_template('common/base.html')


@main.route('/systemInfo', methods=['GET'])
def getSystemInfo():
    response = {
        "cpu_usage": psutil.cpu_percent(0),
        "ram_usage": psutil.virtual_memory().percent
    }
    return json.dumps(response)