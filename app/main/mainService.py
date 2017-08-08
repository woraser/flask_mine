#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/8/8
# Title:
# Tip:
from flask_login import current_user
from app.models import Topic
from peewee import Expression

# 标记该主题已被使用
def markedTopicSign(id):
    res = None
    try:
        account = current_user.account
        res = Topic.update({Topic.user: account, Topic.is_used: True}).where(Topic.id == id).execute()
    except Exception:
        res = None
        pass
    finally:
        return res
    pass


if __name__ == '__main__':
    topicModel = Topic()


    pass