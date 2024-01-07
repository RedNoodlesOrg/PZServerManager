# Made by Fakeapate

import requests
import json
import re


def _listToKV(lst):
    return {f"publishedfileids[{i}]": v for i, v in enumerate(lst)}


def _getCollectionDetails(publishedFileIds):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/"
    payload = {
        "collectioncount": len(publishedFileIds),
        **_listToKV(publishedFileIds),
    }
    response = requests.post(url, data=payload)
    return json.loads(response.text)["response"]


def _getPublishedFileDetails(publishedFileIds):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/"
    payload = {
        "itemcount": len(publishedFileIds),
        **_listToKV(publishedFileIds),
    }
    response = requests.post(url, data=payload)
    return json.loads(response.text)["response"]


def _extractId(text):
    match = re.search(r"Mod\s?ID:\s*(.*?)(\r|\[/hr\]|$)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None


def _getMods(fileDetails: dict):
    mods = []
    for file in fileDetails["publishedfiledetails"]:
        modId = _extractId(file["description"])
        workshopId = file["publishedfileid"]
        thumbnail = file["preview_url"]
        name = file["title"]
        mods.append({
            "modId": modId,
            "workshopId": workshopId,
            "thumbnail": thumbnail,
            "name": name,
        })
    return mods


class SteamCollection:
    _mods: list = []

    @staticmethod
    def update(collection: int | str):
        collectionDetails = _getCollectionDetails([collection])

        fileIds = [
            item["publishedfileid"]
            for item in collectionDetails["collectiondetails"][0]["children"]
        ]

        fileIds_withSort = {
            item["publishedfileid"]: item["sortorder"]
            for item in collectionDetails["collectiondetails"][0]["children"]
        }

        fileDetails = _getPublishedFileDetails(fileIds)
        SteamCollection._mods = _getMods(fileDetails)
        SteamCollection._mods = sorted(
            SteamCollection._mods,
            key=lambda mod: fileIds_withSort.get(mod["workshopId"], float("inf")),
        )
        pass

    @staticmethod
    def getCollection(collection: int | str):
        if not SteamCollection._mods:
            SteamCollection.update(collection)
        return SteamCollection._mods
