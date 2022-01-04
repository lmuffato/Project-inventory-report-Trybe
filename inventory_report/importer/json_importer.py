import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
