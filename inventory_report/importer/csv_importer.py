import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file_to_read):
        if file_to_read.endswith(".csv"):
            with open(file_to_read) as file:
                return list(csv.DictReader(file))
        raise ValueError("Arquivo inválido")
