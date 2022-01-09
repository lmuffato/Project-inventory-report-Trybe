from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith("csv"):
            with open(path, "r") as file:
                data = csv.DictReader(file)
                return list(data)
        else:
            raise ValueError("Arquivo inválido")
