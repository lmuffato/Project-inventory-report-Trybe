from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory():
    def import_data(path, report_type):
        if path.endswith('.csv'):
            with open(path) as file:
                dictionary_obj = csv.DictReader(file)
                dictionary_list = []
                for lists in dictionary_obj:
                    dictionary_list.append(lists)
            if (report_type == "simples"):
                return SimpleReport.generate(dictionary_list)
            else:
                return CompleteReport.generate(dictionary_list)
