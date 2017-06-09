#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for, flash, session
from . import auth
from ..models import User
import json,ConfigParser
from userService import getUserTable



@auth.route('/login', methods=['GET', 'POST'])
def login():
    reponse={}
    reponse["status"] = 0
    if request.method == 'POST':
        post_data = request.values
        login_account = str(post_data['login_account'])
        login_pwd = str(post_data['login_pwd'])
        user = User.getUserByAccountAndPwd(login_account, login_pwd)
        if user is not None:
            session.setdefault('is_login', True)
            session.setdefault('user', json.dumps(user._data))
            reponse['status'] = 1
            reponse['data'] = '/index'
            return json.dumps(reponse)
        else:
            return json.dumps(reponse)
    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))

@auth.route('/userManager')
def userManager():
    return render_template('auth/userManager.html')

@auth.route('/userTable')
def userTable():
    users = getUserTable()
    # TODO users无法转化为json
    return json.dumps(users)


