import csv
import os
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        arquivo, extensao = os.path.splitext(path)
        if extensao != ".csv":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            reader = csv.DictReader(file)
            list = []
            for items in reader:
                list.append(items)
        return list
