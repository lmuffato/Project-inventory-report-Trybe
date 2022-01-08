from typing import Counter
from inventory_report.reports.simple_report import SimpleReport
# from simple_report import SimpleReport


class CompleteReport:

    def products_stock_count(products):
        return Counter([product['nome_da_empresa'] for product in products])

    def generate(products):
        simple_report = SimpleReport.generate(products)
        counter = CompleteReport.products_stock_count(products)

        products_count_str = (
            '\n'
            'Produtos estocados por empresa: \n'
        ) + ''.join([f'- {key}: {counter[key]}\n' for key in counter])

        return simple_report + products_count_str

# import inventory_report.importer.json_importer as imp
# impo = imp.JsonImporter()
# json = impo.readFile('inventory_report/data/inventory.json')

# print(CompleteReport.generate(json))
