"""file_parser.py"""
import re
import glob

from models.log import FACTORY, Log

REGEX_TIMESTAMP = r"(?P<timestamp>\d{2}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3})"
REGEX_LEVEL = r"(?P<level>\w+)"
REGEX_COORDINATES = r"(?P<coordinates>(\d+,?){3})"
REGEX_MESSAGE = r"(?P<message>.*)"
REGEX_STEAMID = r"(?P<steam_id>\d{1,19})"
REGEX_USERNAME = r"(?P<username>.+)"
REGEX_CONTAINER = r"(?P<container>\w+)"
REGEX_ACTION = r"(?P<action>.+)"


def parse_log_line(logtype: str, logline: str) -> Log | None:
    """parse_log_line"""
    log_type = FACTORY[logtype]
    pattern_match = log_type.PARSER.match(logline)
    if pattern_match:
        result = pattern_match.groupdict()
        return FACTORY[logtype].from_dict(log_type, result)
    return None


results = glob.glob('S:\\PythonPs\\pz-server-manager\\tests\\Logs\\*\\*.txt')
logname_pattern = re.compile(
    r".*\d{2}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}_(?P<logfile>.+)\.txt")
for result in results:
    print(f"[FILE] {result}")
    match = logname_pattern.match(result)
    if match is not None:
        parser_name = match.group("logfile")
        with open(result, "r", encoding="utf-8") as file:
            lines = file.readlines()
        PREFIX = ""
        for i, line in enumerate(lines):
            if line.endswith('.\n'):
                parsed = parse_log_line(
                    parser_name, (PREFIX+line).replace('\n', ''))
                print(parsed)
                PREFIX = ""
            else:
                PREFIX += line
