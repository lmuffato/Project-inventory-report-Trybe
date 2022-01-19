import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith("json"):
            raise ValueError("Arquivo inválido")
        content = []
        with open(path, 'r', encoding='utf8') as json_file:
            content = json.load(json_file)
        return content