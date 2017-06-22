#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/21
# Title:
# Tip:
from app.models import User
from peewee import Expression
from app.common.dbFactory import findOneByCondition
from app.commonUtil import convertDbObjToDict
from app.decoratorUtil import catchDbException

def getUserByAccountAndPwd(account, pwd):
    user = findUserByAccountAndPwd(account, pwd)
    # if user:
    #     user = convertDbObjToDict(user,User)
    return user
    pass

@catchDbException
def findUserByAccountAndPwd(account, pwd):
    return User.get(account=account, pwd=pwd)


