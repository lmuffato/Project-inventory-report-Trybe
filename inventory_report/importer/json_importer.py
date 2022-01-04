from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file):
        if file.endswith(".json"):
            with open(file, "r") as jsonfile:
                return json.load(jsonfile)

        raise ValueError("Arquivo inválido")
