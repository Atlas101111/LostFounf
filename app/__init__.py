from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class

from app import secure
from app.api import api
from app.models import db
from app.models.found_info import FoundInfo
from app.models.lost_info import LostInfo

login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)


class JSONEncoder(_JSONEncoder):   # rewrite the default JSONEncoder to support the Jsonify progress
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)


class Flask(_Flask):   # reload the JSONEncoder
    json_encoder = JSONEncoder
    pass


def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    login_manager.init_app(app)
    # login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    db.init_app(app)
    db.create_all(app=app)   # must set value of attr 'app'

    patch_request_class(app, app.config['UPLOADED_UPPER_LIMIT'])
    configure_uploads(app, photos)
    return app


def register_blueprint(app):
    from app.web import web
    print('开始注册蓝图')
    app.register_blueprint(api)
    app.register_blueprint(web)
