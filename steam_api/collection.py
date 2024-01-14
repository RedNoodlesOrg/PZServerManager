"""collection.py"""
import json
from dataclasses import dataclass

from requests import post

from steam_api.mod import Mod
from steam_api.utilities import (get_collection_details, get_mods_from_details,
                                 get_published_file_details)
from pz_server_manager.server.db.mod import sync


@dataclass
class Collection:
    """Collection"""
    mods: list[Mod]
    collection_id: int | str

    @staticmethod
    def _call_api(url: str, payload):
        """call_api"""
        response = post(url, data=payload, timeout=5)
        return json.loads(response.text)["response"]

    def __init__(self, collection_id: str):
        file_ids = [
            item["publishedfileid"]
            for item in get_collection_details([collection_id])[
                "collectiondetails"][0]["children"]
        ]
        self.mods = get_mods_from_details(get_published_file_details(file_ids))
        sync(self.mods)
