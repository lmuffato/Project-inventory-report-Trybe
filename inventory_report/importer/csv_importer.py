from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    @classmethod
    def import_data(self, path):
        if path.endswith("csv"):
            file = open(path, "r")
            data = csv.DictReader(file)
            return list(data)
        else:
            raise ValueError("Arquivo inválido")
