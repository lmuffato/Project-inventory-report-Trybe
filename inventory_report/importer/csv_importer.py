from .importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(data):
        if data.endswith('.csv'):
            with open(data) as file:
                return list(csv.DictReader(file))
        raise ValueError('inválido')
