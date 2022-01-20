import csv
from .importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith('.csv'):
            with open(path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = [line for line in csv_reader]
                return data
        else:
            raise ValueError('Arquivo inválido')
