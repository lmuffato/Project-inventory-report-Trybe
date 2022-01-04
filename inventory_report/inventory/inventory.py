import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, report_type):
        with open(path, mode='r') as csv_file:
            report_data = csv.DictReader(csv_file)
            report = [row for row in report_data]

        if report_type == 'simples':
            return SimpleReport.generate(report)
        if report_type == 'completo':
            return CompleteReport.generate(report)
        else:
            raise ValueError('Invalid report type')
