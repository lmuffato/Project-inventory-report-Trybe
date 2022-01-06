import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(name):
        if name.endswith(".json"):
            with open(name, "r") as jsonfile:
                return json.load(jsonfile)
        raise ValueError("Arquivo inválido")