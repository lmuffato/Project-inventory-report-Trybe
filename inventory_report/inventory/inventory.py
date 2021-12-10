import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type="simples"):
        enterprises_list = []
        if file_path.endswith(".csv"):
            with open(file_path) as file:
                file_reader = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                for enterprise in file_reader:
                    enterprises_list.append(enterprise)
        elif file_path.endswith(".json"):
            with open(file_path) as file:
                enterprises_list = json.load(file)
        if report_type == "simples":
            return SimpleReport.generate(enterprises_list)
        return CompleteReport.generate(enterprises_list)
