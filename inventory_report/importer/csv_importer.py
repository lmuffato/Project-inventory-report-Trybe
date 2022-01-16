import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        products = []
        file_type = path.split('.')[-1]

        if (file_type != 'csv'):
            raise(ValueError('Arquivo inválido'))

        with open(path) as file:
            products_csv = csv.DictReader(file)
            for product in products_csv:
                products.append(product)
        return products
