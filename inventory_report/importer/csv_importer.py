import csv
from .importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if '.csv' in path:
            with open(path, encoding='utf-8') as file:
                return list(csv.DictReader(file))
        raise ValueError('Arquivo inválido')
