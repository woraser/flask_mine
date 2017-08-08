#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# from app.models import User
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]


from app import create_app
from flask_script import Manager, Shell

app = create_app()
manager = Manager(app)



# start the app when execute command:python manage.py runserver
if __name__ == '__main__':
    manager.run()
    # 避免debug模式下二次初始化数据 但是文件更新之后不会在刷新文件
    # app.run(port=5000, debug=True, use_reloader=False)
    #     等同于 判断WERKZEUG_RUN_MAIN 变量 再决定是否运行app
    #     if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    #         pass
    #     app.run(port=5000, debug=True)


