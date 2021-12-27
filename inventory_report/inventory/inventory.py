import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    def open_csv(path):
        with open(path, mode="r") as file:
            return csv.DictReader(file, delimiter=",", quotechar='"')

    def open_json(path):
        with open(path, mode="r") as file:
            return json.load(file)

    def import_data(self, path, type):
        data = []
        if path.endswith("csv"):
            data = self.open_csv(path)
        elif path.endswith("json"):
            data = self.open_json(path)
        if type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
