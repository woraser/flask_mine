#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..decoratorUtil import catchDbException
from ..models import User, getModelClsByName
from ..commonUtil import convertObjToDict

@catchDbException
def queryTableByCls(cls, offset=0, limit=10):
    return cls.select().offset(offset).limit(limit)

@catchDbException
def queryTotalTableByCls(cls):
    return cls.select().count()

# 根据model类名 获得分页数据
def getTablePageByCls(cla_name, offset=0, limit=10):

    cls = getModelClsByName(cla_name)
    data_array = queryTableByCls(cls, offset, limit)
    count = queryTotalTableByCls(cls)
    res = {}
    res.setdefault("count", count)
    content = []
    if data_array is not None:
        child_array = []
        for data in data_array:
            child_array.append(data)
        content = (convertObjToDict(child_array, cls))
    res.setdefault("data", content)
    return res




@catchDbException
def queryUserTableInDb(offset=0, limit=10):
    return User.select().offset(offset).limit(limit)

@catchDbException
def queryTotalUserTableInDb():
    return User.select().count()

def getUserTable(offset=0, limit=10):
    users = queryUserTableInDb(offset, limit)
    if users is None:
        return None
    else:
        user_data = []
        for user in users:
            user_data.append(user)
        return user_data


