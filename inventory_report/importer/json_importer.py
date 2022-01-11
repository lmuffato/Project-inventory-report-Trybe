import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if '.json' in path:
            with open(path, encoding='utf-8') as file:
                return json.load(file)
        raise ValueError('Arquivo inválido')
