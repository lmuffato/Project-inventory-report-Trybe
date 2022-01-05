import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(fileName):
        if not fileName.endswith('json'):
            raise ValueError("Arquivo inválido")
        with open(fileName, 'r') as jsonFile:
            return json.load(jsonFile)

# funcao
