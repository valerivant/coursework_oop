import json


def read_json():
    """функция чтения json"""
    with open("../data/operations.json", "r", encoding='utf-8') as file:
        json_file = file.read()
        result = json.loads(json_file)
    return result

