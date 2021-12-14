import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, report_type):
        dict = []
        with open(path, 'r') as data:
            for line in csv.DictReader(data):
                dict.append(line)
        if (report_type == 'simples'):
            return SimpleReport.generate(dict)
        else:
            return CompleteReport.generate(dict)
