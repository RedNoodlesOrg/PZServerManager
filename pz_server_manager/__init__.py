"""
Edited by Fakeapate
"""

from flask import Flask

from .config import CurrentConfig
from .routes import blueprint


def create_app():
    """create_app"""
    app = Flask(__name__)
    app.config.from_object(CurrentConfig())
    app.register_blueprint(blueprint)
    return app
