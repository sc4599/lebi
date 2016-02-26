# coding=utf-8
from flask import Flask
from application.views.frontend import frontend_blueprint
from application.views.user import user_blueprint
from application.extensions.database import db


def create_app(cfg):
    app = Flask(__name__)
    app.config.from_pyfile(cfg)
    configure_blueprints(app)
    configure_extensions(app)
    return app


def configure_blueprints(app):
    app.register_blueprint(frontend_blueprint)


def configure_extensions(app):
    db.init_app(app)
