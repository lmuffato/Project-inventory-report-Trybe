import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(name):
        if name.endswith(".csv"):
            with open(name) as csvfile:
                file = csv.DictReader(csvfile)
                return [row for row in file]
        raise ValueError("Arquivo inválido")
