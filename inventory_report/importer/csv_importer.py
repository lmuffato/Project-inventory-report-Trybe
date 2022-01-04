import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file: str):
        if not file.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(file) as csv_file:
            data = csv.DictReader(csv_file)
            return list(data)
