# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Edited by Fakeapate
"""

import os

from flask import Blueprint, Request, jsonify, render_template, request, g
from jinja2 import TemplateNotFound
from pz_server_manager.server.file_parser.models.log import Chat, LogCollection

from pz_server_manager.server.file_parser.modlist import Modlist
from pz_server_manager.server.file_parser.server_settings import ServerSettings
from steam_api.collection import Collection

from .config import CurrentConfig
from .server.file_parser.file_parser import read_all

blueprint = Blueprint(
    "views",
    __name__,
)


def base_render(file: str, **kwargs):
    """base_render"""
    try:
        return render_template(file, **kwargs)
    except TemplateNotFound:
        return render_template("home/page-404.html"), 404
    except Exception:
        return render_template("home/page-500.html"), 500


@blueprint.route("/cmd/restart", methods=["POST"])
def restart():
    """restart"""
    return jsonify(success=False)


@blueprint.route("/cmd/applymods", methods=["POST"])
def apply_mods():
    """apply_mods"""
    server_settings = ServerSettings(os.path.join(
        CurrentConfig.PZ_SERVER_FOLDER, "Server/servertest.ini"))
    modlist = Modlist(Collection(CurrentConfig.COLLECTION_ID).mods)
    server_settings.update_mods(modlist).save()
    return jsonify(success=True)


@blueprint.route("/")
@blueprint.route("/index")
@blueprint.route("/index.html")
def pz():
    """pz"""
    segment = get_segment(request)
    mods = Collection(CurrentConfig.COLLECTION_ID).mods
    return base_render(
        "home/mods.html", segment=segment, mods=mods, count_mods=len(mods)
    )
@blueprint.route("/logs")
@blueprint.route("/logs.html")
def logs():
    """logs"""
    collection: LogCollection = g.setdefault('collection', read_all())
    log_collection = collection.get([Chat])
    segment = get_segment(request)
    return base_render("home/logs.html", segment=segment, logs = log_collection)
def get_segment(req: Request):
    """Helper - Extract current page name from request"""
    try:
        segment = req.path.split("/")[-1]
        if segment == "":
            segment = "index"
        return segment
    except Exception:
        return None
