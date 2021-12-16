import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_csv(path, _type):
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data

    def import_json(path, _type):
        with open(path, 'r') as file:
            return json.load(file)

    @classmethod
    def import_data(cls, path, type):
        list = []
        if path.endswith('.csv'):
            list = cls.import_csv(path, type)
        if path.endswith('.json'):
            list = cls.import_json(path, type)
        if type == 'simples':
            return SimpleReport.generate(list)
        if type == 'completo':
            return CompleteReport.generate(list)
