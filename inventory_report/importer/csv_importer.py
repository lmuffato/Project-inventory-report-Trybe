import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith("csv"):
            raise ValueError("Arquivo inválido")
        content = []
        with open(path) as csv_file:
            content = list(csv.DictReader(csv_file))
        return content