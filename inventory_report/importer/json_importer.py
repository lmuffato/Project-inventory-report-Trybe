import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        not_json = path.split('.')[-1] != 'json'

        if not_json:
            raise ValueError("Arquivo inválido")

        with open(path) as json_file:
            return json.load(json_file)
