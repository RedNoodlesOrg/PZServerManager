# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Edited by Fakeapate
"""

from . import blueprint
from flask import render_template, request, jsonify
from jinja2 import TemplateNotFound
from SteamCollection import SteamCollection
from ..config import CurrentConfig
from .interactions import interactions


def base_render(file: str, **kwargs):
    try:
        return render_template(file, **kwargs)
    except TemplateNotFound:
        return render_template("home/page-404.html"), 404
    except Exception:
        return render_template("home/page-500.html"), 500


@blueprint.route("/interaction", methods=["POST"])
def interaction():
    data = request.json
    if isinstance(data, dict):
        if data["interaction"]:
            return jsonify(success=True, result=interactions[data["interaction"]]())
    return jsonify(success=False)


def index():
    return base_render("home/index.html", segment="index")


@blueprint.route("/index")
@blueprint.route("/")
@blueprint.route("/mods")
@blueprint.route("/mods.html")
def pz():
    segment = get_segment(request)
    mods = SteamCollection.getCollection(CurrentConfig.COLLECTION_ID)
    return base_render(
        "home/mods.html", segment=segment, mods=mods, count_mods=len(mods)
    )


@blueprint.route("/bc_button.html")
def buttons():
    segment = get_segment(request)
    return base_render("home/bc_button.html", segment=segment)


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split("/")[-1]

        if segment == "":
            segment = "index"

        return segment

    except Exception:
        return None
