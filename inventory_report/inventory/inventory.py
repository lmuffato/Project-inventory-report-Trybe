import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def send_report(report_type, data):
        if report_type == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    def import_data(cls, path, report_type):
        if path.endswith('.csv'):
            with open(path) as file:
                csv_file = csv.DictReader(file)
                data = [line for line in csv_file]
                return cls.send_report(report_type, data)

        elif path.endswith('.json'):
            with open(path, 'r') as file:
                data = json.load(file)
                return cls.send_report(report_type, data)
