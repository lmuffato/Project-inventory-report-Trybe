import json
import os
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        _nome, extensao = os.path.splitext(path)
        if extensao != ".json":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = json.loads(file.read())
            return data
