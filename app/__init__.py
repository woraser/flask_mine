from flask import Flask
from flask_bootstrap import Bootstrap
from models import initDb, User

bootstrap = Bootstrap()
db = initDb()
# quartz = Quartz()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'hard to guessing'
    bootstrap.init_app(app)
    # register routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api')

    return app
