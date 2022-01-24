import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_csv(file_path):
        with open(file_path) as file:
            path_reader = csv.DictReader(file)
            result_data = [result_row for result_row in path_reader]
            return result_data

    def import_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @classmethod
    def import_data(cls, file_path, report_type):
        if file_path.endswith(".csv"):
            data_list = cls.import_csv(file_path)
        elif file_path.endswith(".json"):
            data_list = cls.import_json(file_path)

        if report_type == "completo":
            return CompleteReport.generate(data_list)
        else:
            return SimpleReport.generate(data_list)
