#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_login import UserMixin
from peewee import *
from app import login_manager


db = SqliteDatabase('./flask_mine.db')

def initDb():
    db.create_tables([User, Topic], safe=True)
    User.createdDefaultAccount()
    db.close()

class BaseModel(Model):
    class Meta:
        database = db

# 用户信息
class User(UserMixin, BaseModel):
    id = IntegerField(primary_key=True)
    account = CharField(max_length=20)
    pwd = CharField(max_length=200)

    # 添加默认账号
    @staticmethod
    def createdDefaultAccount():
        default_account = "chenhui"
        default_pwd = "charles"

        default_account_z = "zhaoshuang"
        default_pwd_z = "shona"

        user = User.getUserByAccountAndPwd(default_account, default_pwd)
        if user is not None:
            return
            pass
        else:
            row = {
                "account": default_account,
                "pwd": default_pwd
            }
            User.insert(row).execute()
        # 第二个账号
        user_z = User.getUserByAccountAndPwd(default_account_z, default_pwd_z)
        if user_z is not None:
            return
            pass
        else:
            row_zs = {
                "account": default_account_z,
                "pwd": default_pwd_z
            }
            User.insert(row_zs).execute()
        pass

    # 根据账号密码获取用户信息
    @staticmethod
    def getUserByAccountAndPwd(account, pwd):
        user_instance = User()
        try:
            user = user_instance.get(User.account == account and User.pwd == pwd)
        except Exception as err:
            # err.message
            user = None
        return user

# 文本信息
class Topic(BaseModel):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=200)
    is_used = BooleanField(default=False)
    is_show = BooleanField(default=True)
    # score = CharField(max_length=10, default="")
    user = CharField(max_length=200, default="")

    @staticmethod
    def checkExit(title):
        TopicInstance = Topic()
        try:
            top = TopicInstance.get(Topic.title==title)
        except Exception as err:
            # err.message
            top = None
        return top
        pass

    @staticmethod
    def addNewTopic(title):
        isExit = Topic.checkExit(title)
        if isExit:
            pass
        else:
            row = {
                "title": title
            }
            TopicInstance = Topic()
            TopicInstance.insert(row).execute()
        pass


@login_manager.user_loader
def load_user(user_id):
    return User.get(id=user_id)

