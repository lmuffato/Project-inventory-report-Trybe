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

    # necessidade de identificar classmethod e trocar self por cls vista
    # no repositório do Jodiel e no stackoverflow
    # https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes

    @classmethod
    def import_data(cls, path, type):
        data = []
        if path.endswith("csv"):
            data = cls.open_csv(path)
        elif path.endswith("json"):
            data = cls.open_json(path)
        if type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
