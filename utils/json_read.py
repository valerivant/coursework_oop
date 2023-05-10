import json


def read_json():
    with open("./operations.json", "r", encoding='utf-8') as file:
        json_file = file.read()
        result = json.loads(json_file)
    return result

