from flask import Flask

from .config import Config, db, login_manager
from .controllers import common, login, user, slot, frame, examplyar, sintez


def create_app():
    es_app = Flask(__name__)
    es_app.config.from_object(Config)

    db.init_app(es_app)

    login_manager.init_app(es_app)
    login_manager.login_view = 'login.login_func'
    login_manager.login_message_category = 'info'

    es_app.register_blueprint(common)
    es_app.register_blueprint(login)
    es_app.register_blueprint(user)
    es_app.register_blueprint(slot)
    es_app.register_blueprint(frame)
    es_app.register_blueprint(examplyar)
    es_app.register_blueprint(sintez)

    return es_app
