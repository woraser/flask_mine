#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/13
# Title:
# Tip:
import apiService
import app.commonUtil as util
from . import api

@api.route("/initTopic", methods=['GET'])
def importDefaultTopics():
    apiService.importDefaultTopic()
    return util.buildSucc("初始化成功")
    pass