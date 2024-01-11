"""file_parser.py"""
import os
import re
import glob

from pz_server_manager.server.file_parser.models.log import FACTORY, LogCollection, LogVar
from pz_server_manager.config import CurrentConfig

REGEX_TIMESTAMP = r"(?P<timestamp>\d{2}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3})"
REGEX_LEVEL = r"(?P<level>\w+)"
REGEX_COORDINATES = r"(?P<coordinates>(\d+,?){3})"
REGEX_MESSAGE = r"(?P<message>.*)"
REGEX_STEAMID = r"(?P<steam_id>\d{1,19})"
REGEX_USERNAME = r"(?P<username>.+)"
REGEX_CONTAINER = r"(?P<container>\w+)"
REGEX_ACTION = r"(?P<action>.+)"


def parse_log_line(logtype: str, logline: str) -> LogVar | None:
    """Parse Log Line"""
    log_class = FACTORY.get(logtype)
    if log_class:
        pattern = log_class.PARSER
        pattern_match = pattern.match(logline)
        if pattern_match:
            return log_class.from_dict(log_class, pattern_match.groupdict())
    return None




def read_file(filename: str, parser_name: str, collection: LogCollection) -> list:
    """reads a logfile"""

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    logs: list = []
    prefix = ""
    for line in lines:
        if line.endswith('.\n'):
            parsed = parse_log_line(
                parser_name, (prefix+line).replace('\n', ''))
            if parsed is not None:
                collection.add(parsed)
            prefix = ""
        else:
            prefix += line
    return logs


def read_all() -> LogCollection:
    """Read all .txt files in the Logs folder"""
    collection: LogCollection = LogCollection()
    results = glob.glob(os.path.join(CurrentConfig.PZ_SERVER_FOLDER, "Logs\\*\\*.txt"))
    logname_pattern = re.compile(
        r".*\d{2}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}_(?P<logfile>.+)\.txt")
    for result in results:
        match = logname_pattern.match(result)
        if match is not None:
            read_file(result, match.group("logfile"), collection)

    return collection
