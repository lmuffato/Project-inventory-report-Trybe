import csv

from .importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(data):
        if not data.endswith('.csv'):
            raise ValueError('Extensão de Arquivo inválido')
        with open(data) as file:
            return list(csv.DictReader(file))
