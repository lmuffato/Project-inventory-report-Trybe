import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file: str):
        if(not file.endswith(".json")):
            raise ValueError("Arquivo inválido")
        with open(file) as json_file:
            data = json.load(json_file)
            return data
