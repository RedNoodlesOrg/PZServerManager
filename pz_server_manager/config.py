# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Edited by Fakeapate
"""

import os


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    # Assets Management
    ASSETS_ROOT = os.getenv("ASSETS_ROOT", "/static/assets")
    RCON_PW = os.getenv("RCON_PW", "")
    RCON_HOST = os.getenv("RCON_HOST", "")
    RCON_PORT = os.getenv("RCON_PORT", 27015)
    COLLECTION_ID = os.getenv("COLLECTION_ID", 3126799274)
    PZ_SERVER_FOLDER = os.getenv("PZ_SERVER_FOLDER", "")


class ProductionConfig(Config):
    DEBUG = False
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DebugConfig(Config):
    DEBUG = True


class CurrentConfig(DebugConfig):
    pass
