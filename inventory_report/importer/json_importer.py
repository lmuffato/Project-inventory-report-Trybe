import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(file_to_read):
        if file_to_read.endswith(".json"):
            with open(file_to_read) as file:
                return json.load(file)
        raise ValueError("Arquivo inválido")
