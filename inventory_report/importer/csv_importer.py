import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith(".csv"):
            with open(path, mode="r") as file:
                data = csv.DictReader(file)
                return [*data]
        raise ValueError("Arquivo inválido")