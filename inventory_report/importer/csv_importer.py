import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if not path.endswith('csv'):
            raise ValueError('Arquivo inválido')
        result = []
        with open(path) as csv_file:
            products_list = csv.DictReader(csv_file, delimiter=',')
            for product in products_list:
                result.append(product)
        return result
