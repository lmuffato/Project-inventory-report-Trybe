from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    def read_json(path):
        with open(path) as file:
            reader = json.load(file)
            return reader

    @staticmethod
    def import_data(file):
        path = file.split('.')
        extension = path[-1]
        if (extension != "json"):
            raise ValueError('Arquivo inválid')
        file_read = JsonImporter.read_json(file)
        return file_read
