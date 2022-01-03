from .importer import Importer
import csv


class CsvImporter(Importer):

    def import_data(path):
        with open(path) as file:
            if('csv' in path):
                csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
                header, *data = csv_file
                data = [header, *data]
                return data
            else:
                raise ValueError('Arquivo inválido')
