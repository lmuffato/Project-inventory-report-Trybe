import csv
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
            with open(path) as data:
                csv_reader = csv.DictReader(data)
                data = [line for line in csv_reader]
                return cls.send_report(report_type, data)
