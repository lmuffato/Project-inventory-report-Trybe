import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read_csv(path):
        list = []
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            for value in reader:
                list.append(value)
        return list

    def read_json(path):
        with open(path) as json_file:
            return json.load(json_file)

    @classmethod
    def import_data(cls, path, report_type):
        readers = {
            "csv": cls.read_csv,
            "json": cls.read_json
        }

        reports = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate
        }

        file_format = path.split('.')[-1]
        list = readers[file_format](path)
        return reports[report_type](list)
