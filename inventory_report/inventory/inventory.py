import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, report_type):
        if path.endswith('.csv'):
            with open(path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = [line for line in csv_reader]
                if report_type == 'simples':
                    return SimpleReport.generate(data)
                else:
                    return CompleteReport.generate(data)
