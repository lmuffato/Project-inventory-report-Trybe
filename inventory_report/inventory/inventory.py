import json
import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_json(path):
        with open(path, mode="r") as file:
            return json.load(file)

    def import_csv(path):
        with open(path, mode="r") as file:
            [*data] = csv.DictReader(file, delimiter=",", quotechar='"')
            return data

    @classmethod
    def import_data(cls, path, type):
        list = []
        if path.endswith(".json"):
            list = cls.import_json(path)
        if path.endswith(".csv"):
            list = cls.import_csv(path)
        if type == "completo":
            return CompleteReport.generate(list)
        return SimpleReport.generate(list)
