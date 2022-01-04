from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file):
        if file.endswith(".csv"):
            with open(file) as csvfile:
                read = csv.DictReader(csvfile)
                return [row for row in read]
        raise ValueError("Arquivo inválido")
