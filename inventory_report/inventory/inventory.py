import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    __report_type = {
      "simples": SimpleReport.generate,
      "completo": CompleteReport.generate,
    }

    data_content = []

    def import_data(path, type):
        if path.endswith(".csv"):
            with open(path) as csvfile:
                file = csv.DictReader(csvfile)
                data_content = [row for row in file]

        elif path.endswith(".json"):
            with open(path) as jsonfile:
                data_content = json.load(jsonfile)

        return Inventory.__report_type[type](data_content)


# Checagem com a terminação do arquivo
# https://www.programiz.com/python-programming/methods/string/endswith
