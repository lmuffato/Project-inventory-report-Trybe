from .importer import Importer
import json
import os


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_name, extension = os.path.splitext(path)

        if extension != ".json":
            raise ValueError("Arquivo inválido")

        with open(path) as jsonFile:
            return json.load(jsonFile)
