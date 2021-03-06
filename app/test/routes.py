#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/13
# Title:
# Tip:
from flask import jsonify
from . import test
from ..models import User
from ..common.dbFactory import batchInsert
import time

@test.route("/testpeewee")
def testpeewee():
    format_time = time.time()
    insert_datas = [{"account": "123", "pwd": "123", "created_time": format_time},
                    {"account": "1234", "pwd": "1234", "created_time": format_time},
                    {"account": "12345", "pwd": "12345", "created_time": format_time}]
    res = batchInsert("User", insert_datas)
    return jsonify({"status":1})
    pass




