#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/21
# Title:
# Tip:
from flask_login import LoginManager
from flask import Flask
from flask_bootstrap import Bootstrap

# 初始化中间件
bootstrap = Bootstrap()
login_manager = LoginManager()
# 登录管理信息
login_manager.session_protection = 'hehenopwd'
login_manager.login_view = 'auth.login'
login_manager.login_message = "请登录！"

def create_app():
    app = Flask(__name__)
    app.secret_key = 'hard to guessing13459'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chenhui.db'
    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    from models import initDb
    db = initDb()
    # session.permanent = True
    # db.init_app(app)
    # # init default table
    # with app.app_context():
    #     import sqlModels
    #     # Extensions like Flask-SQLAlchemy now know what the "current" app
    #     # is while within this block. Therefore, you can now run........
    #     db.create_all()
    # #
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db = initDb()
    # register routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .common import common as common_blueprint
    app.register_blueprint(common_blueprint, url_prefix='/common')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api')

    from .test import test as test_blueprint
    app.register_blueprint(test_blueprint, url_prefix='/test')

    return app
