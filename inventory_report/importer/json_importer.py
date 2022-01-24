import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(import_file):
        with open(import_file, "r") as file:
            if not import_file.endswith(".json"):
                raise ValueError("Arquivo inválido")

            return json.load(file)
