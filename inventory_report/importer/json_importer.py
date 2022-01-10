from .importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(data):
        if data.endswith('.json'):
            with open(data) as file:
                return json.load(file)
        else:
            raise ValueError('inválido')
