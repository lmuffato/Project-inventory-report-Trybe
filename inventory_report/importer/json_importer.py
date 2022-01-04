from .importer import Importer
import json


class JSON_Importer(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as jsonFile:
            return json.load(jsonFile)
