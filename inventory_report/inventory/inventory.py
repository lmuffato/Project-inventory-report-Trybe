from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def verify_extension(cls, path):
        if path.endswith('.csv'):
            with open(path) as file:
                data_reader = csv.DictReader(file)
                data = [item for item in data_reader]
            return data
        elif path.endswith('.json'):
            with open(path) as file:
                data_reader = json.load(file)
                data = [item for item in data_reader]
            return data
        elif path.endswith('.xml'):
            with open(path) as file:
                data_reader = xmltodict.parse(file.read())
                data = [item for item in data_reader['dataset']['record']]
            return data

    @classmethod
    def import_data(cls, path, type):
        extension_data = cls.verify_extension(path)
        if (type == 'simples'):
            return SimpleReport.generate(extension_data)
        elif (type == 'completo'):
            return CompleteReport.generate(extension_data)

#  Fonte para xmltodict:https://python-guide-pt-br.readthedocs.io/
# pt_BR/latest/scenarios/xml.html
