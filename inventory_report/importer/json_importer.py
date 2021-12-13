import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        file_data = []

        with open(file_path) as file:
            file_data = json.load(file)

        return file_data
