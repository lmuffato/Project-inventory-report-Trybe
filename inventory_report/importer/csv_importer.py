import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(import_file):
        with open(import_file) as file:
            if not import_file.endswith(".csv"):
                raise ValueError("Arquivo inválido")

            path_reader = csv.DictReader(file)
            result_data = [result_row for result_row in path_reader]
            return result_data
