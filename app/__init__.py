#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/21
# Title:
# Tip:
from flask_login import LoginManager
from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'hehenopwd'
login_manager.login_view = 'auth.login'
login_manager.login_message = "请登录！"

def create_app():
    app = Flask(__name__)
    app.secret_key = 'hard to guessing13459'
    # session.permanent = True
    bootstrap.init_app(app)
    login_manager.init_app(app)
    from models import initDb
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
