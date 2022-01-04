import json
import os
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        _arquivo, extensao = os.path.splitext(path)
        if extensao != ".json":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            content = file.read()
            list = json.loads(content)
            for item in list:
                if "record" in item:
                    del item["record"]
            return list
