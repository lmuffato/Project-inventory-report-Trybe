from .importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if ".json" in path:
            with open(path) as file:
                list = json.load(file)
            return list
        else:
            raise ValueError('Arquivo inválido')
