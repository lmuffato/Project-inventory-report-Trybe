import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith('.csv'):
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            return list(csv.DictReader(file))
