"""modlist.py"""

from steam_api.mod import Mod
from steam_api.utilities import (get_mods_from_details,
                                 get_published_file_details)


class Modlist():
    """Modlist"""
    mods: list[Mod] | None
    modids: str | None
    workshopids: str | None

    def __init__(self,
                 mods: list[Mod] | None = None,
                 modids: str | None = None,
                 workshopids: str | None = None):
        if mods is None:
            if modids is None or workshopids is None:
                raise ValueError("Cannot leave out mods and ids!")
        else:
            if modids is not None or workshopids is not None:
                raise ValueError("Cannot set mods and ids!")
        self.mods = mods
        self.modids = modids
        self.workshopids = workshopids

    def get_ids(self) -> tuple[str, str]:
        """get_modids"""
        if self.modids is None or self.workshopids is None:
            if self.mods:
                self.modids = ";".join(
                    [str(mod.mod_id) for mod in self.mods])
                self.workshopids = ";".join(
                    [mod.workshop_id for mod in self.mods])
            else:
                raise ValueError("mods not set!")
        return self.modids, self.workshopids

    def get_mods(self):
        """get_mods"""
        if self.mods is None and self.workshopids is None:
            raise ValueError("either mods or workshopids needs to be set!")
        if self.mods is None and self.workshopids is not None:
            workshopids = self.workshopids.split(";")
            self.mods = get_mods_from_details(get_published_file_details(workshopids))
        return self.mods
