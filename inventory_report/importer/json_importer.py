import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith('.json'):
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            return json.load(file)
