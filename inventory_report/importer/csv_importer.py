# Feito por minha dupla Nathalia Zebral
from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file_path):
        if file_path.endswith(".csv"):
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                return [row for row in reader]
        raise ValueError("Arquivo inválido")
