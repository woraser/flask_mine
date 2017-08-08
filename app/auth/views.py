#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
import authService
from . import auth
from app.commonUtil import buildErr,buildSucc,buildNone
import json


@auth.route('/login', methods=['GET', 'POST'])
def login():
    reponse={}
    reponse["status"] = 0
    if request.method == 'POST':
        post_data = json.loads(request.data)
        login_account = post_data['login_account']
        login_pwd = post_data['login_pwd']
        user = authService.getUserByAccountAndPwd(login_account,login_pwd)

        if user is not None:
            login_user(user, True)
            return buildSucc('/index')
        else:
            return buildErr("no user")
    return render_template('auth/login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))

@auth.route('/userManager')
@login_required
def userManager():
    return render_template('auth/userManager.html')