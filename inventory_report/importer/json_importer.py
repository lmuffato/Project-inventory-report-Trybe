import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith('.json'):
            with open(path, 'r') as file:
                data = json.load(file)
                return data
        else:
            raise ValueError('Arquivo inválido')
