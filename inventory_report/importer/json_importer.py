import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if ".json" in path:
            with open(path) as file:
                list_from_json = json.load(file)
                return list_from_json
        raise ValueError("Arquivo inválido")
