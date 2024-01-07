# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Edited by Fakeapate
"""

from flask import Flask
from .config import DebugConfig
from .home import routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(DebugConfig())
    app.register_blueprint(routes.blueprint)
    return app
