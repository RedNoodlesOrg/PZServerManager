"""mod.py"""

import re
from dataclasses import dataclass


def extract_id(text) -> str | None:
    """extract_id"""
    match = re.search(r"Mod\s?ID:\s*(.*?)(\r|\[/hr\]|$)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None


@dataclass
class Mod():
    """Mod"""
    workshop_id: str
    mod_id: str | None
    thumbnail: str
    name: str

    def __init__(self, workshop_details: dict):
        """__init__"""
        self.mod_id = extract_id(workshop_details["description"])
        self.workshop_id = workshop_details["publishedfileid"]
        self.thumbnail = workshop_details["preview_url"]
        self.name = workshop_details["title"]
