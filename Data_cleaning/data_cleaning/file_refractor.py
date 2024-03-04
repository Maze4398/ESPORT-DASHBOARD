import json
from datetime import datetime


def fix_format_json(json_file, indent, enc):
    with open(json_file, 'r', encoding=enc) as f:
        data = json.load(f)

    with open(json_file, 'w', encoding=enc) as f:
        json.dump(data, f, indent=indent)


json_file = 'JSON\\proMatches.json'
indent = 4
enc = 'utf-8'

fix_format_json(json_file,indent,enc)

def from_unix_to_date(json_file, indent, enc):


def from_unix_to_duration(json_file, indent, enc):