from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        file_error = path.split('.')[-1]
        if file_error != 'json':
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            json_file = json.loads(file.read())
            return json_file
