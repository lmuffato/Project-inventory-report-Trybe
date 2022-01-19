from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):  # implementando o método abstrato
        if (path.endswith('json')):
            stock = []
            with open(path) as file:
                stock_json = json.load(file)
                for elemento in stock_json:
                    stock.append(elemento)
            return stock
        else:
            raise(ValueError('Arquivo inválido'))

# Teste manual
# readJson = JsonImporter.import_data('inventory_report/data/inventory.json')
# print(readJson)
