import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file)
            return [row for row in reader]
