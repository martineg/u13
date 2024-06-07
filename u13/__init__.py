import os
from flask import Flask
from .extensions import db
from .routes import short
from .auth import auth

def create_app(config_file='settings.py', test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(short)
    return app
