#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from peewee import *
from app import login_manager

db = SqliteDatabase('./test3.db')

def initDb():
    db.create_tables([User], safe=True)
    db.close()

class BaseModel(Model):
    class Meta:
        database = db

# 用户信息
class User(UserMixin, BaseModel):
    id = IntegerField(primary_key=True)
    account = CharField(max_length=20)
    pwd = CharField(max_length=200)
    created_time = DateField()


@login_manager.user_loader
def load_user(user_id):
    return User.get(id=user_id)

