import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        file_data = []

        with open(file_path) as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for enterprise in file_reader:
                file_data.append(enterprise)

        return file_data
