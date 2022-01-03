import re
import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(filepath):
        isCsv = re.search(".csv$", filepath)

        if not isCsv:
            raise ValueError("Arquivo inválido")

        with open(filepath, mode="r") as file:
            data = csv.DictReader(file)
            return list(data)
