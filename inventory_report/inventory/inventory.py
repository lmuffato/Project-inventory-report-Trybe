import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        products = []
        with open(path) as file:
            products_csv = csv.DictReader(file)
            for product in products_csv:
                products.append(product)

        if (type == 'simples'):
            return SimpleReport.generate(products)
        elif (type == 'completo'):
            return CompleteReport.generate(products)
