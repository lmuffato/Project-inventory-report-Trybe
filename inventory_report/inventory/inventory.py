import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        with open(path, 'r') as file:
            if path.endswith('.csv'):
                reader = csv.DictReader(file)
                data = [row for row in reader]
            if type == 'simples':
                return SimpleReport.generate(data)
            if type == 'completo':
                return CompleteReport.generate(data)
