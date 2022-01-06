import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read_file(path):
        with open(path) as file:
            if('csv' in path):
                csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
                header, *data = csv_file
                data = [header, *data]
            if('json' in path):
                data = json.load(file)
            return data

    def import_data(path, report_type):
        report_data = Inventory.read_file(path)
        if report_type == 'simples':
            return SimpleReport.generate(report_data)
        if report_type == 'completo':
            return CompleteReport.generate(report_data)
        else:
            raise ValueError('Invalid report type')
