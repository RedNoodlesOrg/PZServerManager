from SteamCollection import SteamCollection
from ..config import CurrentConfig
from flask import render_template

import os


def _fetch_collection():
    SteamCollection.update(CurrentConfig.COLLECTION_ID)
    return render_template(
        "includes/modlist.j2",
        mods=SteamCollection.getCollection(CurrentConfig.COLLECTION_ID),
    )


def _restart_server():
    pass


def _apply_collection():
    with open(
        os.path.join(CurrentConfig.PZ_SERVER_FOLDER, "Server/servertest.ini"),
        "r",
        encoding="utf-8",
    ) as configfile:
        lines = configfile.readlines()
    found_indices = {"Mods=": -1, "WorkshopItems=": -1}

    for i, line in enumerate(lines):
        for search_text in found_indices.keys():
            if line.startswith(search_text) and found_indices[search_text] == -1:
                found_indices[search_text] = i
        if all(index != -1 for index in found_indices.values()):
            break

    mods = SteamCollection.getCollection(CurrentConfig.COLLECTION_ID)
    modids = ";".join([mod["modId"] for mod in mods])
    workshopids = ";".join([mod["workshopId"] for mod in mods])

    lines[found_indices["Mods="]] = f"Mods={modids}"
    lines[found_indices["WorkshopItems="]] = f"WorkshopItems={workshopids}"

    with open(
        os.path.join(CurrentConfig.PZ_SERVER_FOLDER, "Server/servertest.ini"),
        "w",
        encoding="utf-8",
    ) as configfile:
        configfile.writelines(lines)


interactions = {
    "fetch_collection": _fetch_collection,
    "restart_server": _restart_server,
    "apply_collection": _apply_collection,
}
