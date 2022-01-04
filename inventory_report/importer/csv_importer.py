from .importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if ".csv" in path:
            with open(path) as file:
                return list(csv.DictReader(file))
        else:
            raise ValueError('Arquivo inválido')
