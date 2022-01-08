import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        with open(path) as file:
            csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
            header, *data = csv_file
            data = [header, *data]
        if type == 'simples':
            return SimpleReport.generate(data)
        if type == 'completo':
            return CompleteReport.generate(data)
