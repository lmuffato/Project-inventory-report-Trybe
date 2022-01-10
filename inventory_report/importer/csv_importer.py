import csv
from .importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if ".csv" in path:
            with open(path) as file:
                list_from_csv = list(csv.DictReader(file))
                return list_from_csv
        raise ValueError("Arquivo inválido")
