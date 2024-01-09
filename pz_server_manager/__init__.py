"""
Copyright (c) 2019 - present AppSeed.us
Edited by Fakeapate
"""

from flask import Flask

from .config import DebugConfig

from .routes import blueprint


def create_app():
    """create_app"""
    app = Flask(__name__)
    app.config.from_object(DebugConfig())
    app.register_blueprint(blueprint)
    return app
