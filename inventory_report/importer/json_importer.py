import json

from .importer import Importer


class JSONImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_informations = cls.get_file_informations(path)

        if file_informations["file_type"] == '.json':
            with open(path) as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido")
