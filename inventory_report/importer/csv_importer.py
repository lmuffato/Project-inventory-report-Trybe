from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        with open(path, mode="r") as csv_file:
            if path.endswith(".csv"):
                reader = csv.DictReader(csv_file)
                data = [row for row in reader]
                return data
            else:
                raise ValueError("Arquivo inválido")
