import csv
import os
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        nome, extensao = os.path.splitext(path)
        if extensao != ".csv":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            reader = csv.DictReader(file)
            data = []
            for items in reader:
                data.append(items)
        return data
