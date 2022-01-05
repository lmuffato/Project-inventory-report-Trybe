import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        list = []
        not_csv = path.split('.')[-1] != 'csv'

        if not_csv:
            raise ValueError("Arquivo inválido")

        with open(path) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            for value in reader:
                list.append(value)
        return list
