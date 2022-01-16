import csv
import json
import xml.etree.ElementTree as ET
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

    def get_products_from_xml(path):
        products = []
        with open(path) as file:
            products_xml = ET.parse(file).getroot()
            for product in products_xml:
                products.append({
                                    product[0].tag: product[0].text,
                                    product[1].tag: product[1].text,
                                    product[2].tag: product[2].text,
                                    product[3].tag: product[3].text,
                                    product[4].tag: product[4].text,
                                    product[5].tag: product[5].text,
                                    product[6].tag: product[6].text,
                                })
        return products

    @classmethod
    def import_data(cls, path, type):
        products = []
        file_type = path.split('.')[-1]

        if (file_type == 'csv'):
            products = cls.get_products_from_csv(path)
        elif (file_type == 'json'):
            products = cls.get_products_from_json(path)
        else:
            products = cls.get_products_from_xml(path)

        if (type == 'simples'):
            return SimpleReport.generate(products)
        elif (type == 'completo'):
            return CompleteReport.generate(products)
