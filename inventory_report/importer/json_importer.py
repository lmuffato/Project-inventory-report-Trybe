import json


class Json_importer:
    def import_json(path):
        with open(path, "r") as file:
            return json.load(file)
