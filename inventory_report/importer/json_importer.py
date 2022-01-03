import json

from .importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(data):
        if not data.endswith('.json'):
            raise ValueError('Extensão de Arquivo inválido')
        with open(data) as file:
            return json.load(file)
