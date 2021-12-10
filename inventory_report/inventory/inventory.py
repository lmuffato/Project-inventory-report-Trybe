import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type="simples"):
        with open(file_path) as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            enterprises_list = []
            for enterprise in file_reader:
                enterprises_list.append(enterprise)
        if report_type == "simples":
            return SimpleReport.generate(enterprises_list)
        return CompleteReport.generate(enterprises_list)
