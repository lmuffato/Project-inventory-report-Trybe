import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith('.json'):
            with open(path, 'r') as json_file:
                data = json.load(json_file)
                return data
        else:
            raise ValueError('Arquivo inválido')
