from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv

class Inventory():

    @staticmethod
    def import_data(path, report_type):
        with open(path) as file:
            my_data = csv.DictReader(file, delimiter=',', quotechar='"')
            heads, *data = my_data
            obj = [heads, *data]


        if report_type == "simples":
            report = SimpleReport.generate(obj)
            return report

        if report_type == "completo":
            report = CompleteReport.generate(obj)
            return report
