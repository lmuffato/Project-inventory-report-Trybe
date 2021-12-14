import csv
import json
# import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_csv(path):
        dict = []
        with open(path, 'r') as data:
            for line in csv.DictReader(data):
                dict.append(line)
        return dict

    def import_json(path):
        dict = []
        with open(path) as data:
            dict = json.load(data)
        return dict

    @classmethod
    def import_data(my_class, path, report_type):
        data = []
        if (path.endswith('.csv')):
            data = my_class.import_csv(path)
        elif (path.endswith('.json')):
            data = my_class.import_json(path)
        else:
            data = my_class.import_xml(path)
        if (report_type == 'simples'):
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
