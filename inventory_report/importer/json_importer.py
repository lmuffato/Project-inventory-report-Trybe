import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith(".json"):
            with open(path, mode="r") as file:
                data = json.load(file)
                return data
        raise ValueError("Arquivo inválido")
