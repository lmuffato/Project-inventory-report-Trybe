import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def reader_from_csv(path):
        stock = []
        with open(path) as file:
            stock_csv = csv.DictReader(file)
            for row in stock_csv:
                stock.append(row)
        return stock

    def reader_from_json(path):
        stock = []
        with open(path) as file:
            stock_json = json.load(file)
            for row in stock_json:
                stock.append(row)
        return stock

    def reader_from_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()  # Raiz, tag principal
        stock = [
          {elemento.tag: elemento.text for elemento in record}
          # Lista os elementos filhos de record: nome e texto
          for record in root.findall('record')  # buscar tags record
          # record, são as tags que contem os elementos com texto
        ]
        return stock

    @classmethod
    def reader_file(cls, path):
        if (path.endswith(".csv")):
            return cls.reader_from_csv(path)
        elif (path.endswith('json')):
            return cls.reader_from_json(path)
        elif (path.endswith('xml')):
            return cls.reader_from_xml(path)
        else:
            raise ValueError("Invalid File")

    @classmethod
    def import_data(cls, path, type):
        stock = cls.reader_file(path)

        if (type == 'simples'):
            return SimpleReport.generate(stock)
        elif (type == 'completo'):
            return CompleteReport.generate(stock)
        else:
            raise ValueError("Invalid option")

# Teste manual
# x = Inventory.import_data('inventory_report/data/inventory.csv', 'completo')
# y = Inventory.import_data('inventory_report/data/inventory.json', 'completo')
# z = Inventory.import_data('inventory_report/data/inventory.xml', 'completo')
# print(x)
# print(y)
# print(z)
