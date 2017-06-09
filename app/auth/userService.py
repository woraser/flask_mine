#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..decoratorUtil import catchDbException
from ..models import User

@catchDbException
def queryUserTableInDb():
    return User.select()

def getUserTable():
    users = queryUserTableInDb()
    if users is None:
        return None
    else:
        user_data = []
        for user in users:
            user_data.append(user)
        return user_data


