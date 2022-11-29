import json
import re
from typing import TextIO

CSV_CELLS_PATTERN = re.compile('"(""|[^"])*"|(?=,,)|(?=^,)|(?=,$)|[^,]+')

INPUT_FILE_WITH_HEADERS = "biostats.csv"
INPUT_FILE_WITHOUT_HEADERS = "addresses.csv"


def cast(string: str):
    try:
        return int(string)
    except:
        try:
            return float(string)
        except:
            return string if string else None


def csv_to_list_dict(file_path: str, with_headers: bool) -> list[dict]:
    with open(file_path, 'r') as file:
        return to_dicts_with_headers(file) if with_headers \
            else to_dicts_with_enumeration(file)


def to_dicts_with_headers(file: TextIO):
    list_of_dictionaries: list[dict] = []
    headers: list[str] = parse_cells(file.readline())
    for line in file.readlines():
        casted_cells = [cast(cell) for cell in parse_cells(line)]
        dictionary: dict = dict(zip(headers, casted_cells))
        list_of_dictionaries.append(dictionary)
    return list_of_dictionaries


def to_dicts_with_enumeration(file: TextIO) -> list[dict]:
    return [
        {i: cast(e) for i, e in enumerate(parse_cells(line))}
        for line in file.readlines()
    ]


def parse_cells(line: str):
    return [match.group(0) for match in list(CSV_CELLS_PATTERN.finditer(line.strip()))]


print(json.dumps(csv_to_list_dict(INPUT_FILE_WITH_HEADERS, True), indent=5))
print(json.dumps(csv_to_list_dict(INPUT_FILE_WITHOUT_HEADERS, False), indent=5))
