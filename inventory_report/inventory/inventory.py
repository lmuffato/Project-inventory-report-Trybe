import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def read_csv(path):
        dictionary = []
        with open(path, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                dictionary.append(row)
            return dictionary

    def report_type(type, file):
        if type == "simples":
            return SimpleReport.generate(file)
        if type == "completo":
            return CompleteReport.generate(file)

    def read_json(path):
        with open(path) as json_file:
            return json.load(json_file)

    @classmethod
    def import_data(cls, path, type):
        readers = {
            "csv": cls.read_csv,
            "json": cls.read_json
        }

        reports = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate
        }
        format = path.split('.')[-1]
        response = readers[format](path)
        return reports[type](response)
