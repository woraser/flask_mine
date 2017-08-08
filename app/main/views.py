#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, json, session, redirect, url_for, request
from flask_login import login_required, current_user
from . import main
from mainService import markedTopicSign
import app.commonUtil as Util



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

# 标记该主题已被使用
@main.route("/topicMark/<string:id>", methods=['GET'])
def markedTopic(id):
    res = markedTopicSign(id)
    if res is not None:
        return Util.buildSucc("ok")
    else:
        return Util.buildErr("操作失败，请联系管理员！")
    pass


