from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        with open(path, mode="r") as json_file:
            if path.endswith(".json"):
                reader = json.load(json_file)
                return reader
            else:
                raise ValueError("Arquivo inválido")
