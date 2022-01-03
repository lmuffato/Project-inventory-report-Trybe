from .importer import Importer
import json


class JsonImporter(Importer):

    def import_data(path):
        with open(path) as file:
            if('json' in path):
                data = json.load(file)
                return data
            else:
                raise ValueError('Arquivo inválido')
