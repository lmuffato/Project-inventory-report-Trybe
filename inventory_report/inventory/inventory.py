import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        data = []
        with open(path) as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in content:
                data.append(row)
        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
