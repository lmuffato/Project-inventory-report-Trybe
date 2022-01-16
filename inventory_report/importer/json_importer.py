import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        products = []
        fileType = path.split('.')[-1]

        if (fileType != 'json'):
            raise(ValueError('Arquivo inválido'))

        with open(path) as file:
            products_json = json.load(file)
        for product in products_json:
            products.append(product)
        return products
