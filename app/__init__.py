from flask import Flask
from app import secure
from app.api import api
from app.models import db


def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)   # must set value for attr app
    return app


def register_blueprint(app):
    from app.web import web
    print('开始注册蓝图')
    # app.register_blueprint(api)
    app.register_blueprint(web)
