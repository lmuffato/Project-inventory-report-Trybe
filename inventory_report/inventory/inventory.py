import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def get_products_from_csv(path):
        products = []
        with open(path) as file:
            products_csv = csv.DictReader(file)
            for product in products_csv:
                products.append(product)
        return products

    def get_products_from_json(path):
        products = []
        with open(path) as file:
            products_json = json.load(file)
            for product in products_json:
                products.append(product)
        return products

    # def get_products_from_xml(path):
    #     products = []
    #     with open(path) as file:
    #         products_csv = csv.DictReader(file)
    #         for product in products_csv:
    #             products.append(product)
    #     return products

    @classmethod
    def import_data(cls, path, type):
        products = []
        fileType = path.split('.')[-1]

        if (fileType == 'csv'):
            products = cls.get_products_from_csv(path)
        elif (fileType == 'json'):
            products = cls.get_products_from_json(path)

        if (type == 'simples'):
            return SimpleReport.generate(products)
        elif (type == 'completo'):
            return CompleteReport.generate(products)
