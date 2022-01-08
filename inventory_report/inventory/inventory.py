import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        file_extension = path.split(".")[1]
        if file_extension == 'csv':
            with open(path) as file:
                csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
                header, *data = csv_file
                data = [header, *data]
        if file_extension == 'json':
            with open(path) as file:
                data = json.load(file)
        if type == 'simples':
            return SimpleReport.generate(data)
        if type == 'completo':
            return CompleteReport.generate(data)
