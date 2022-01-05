import csv
import json
import xmltodict
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

    def read_xml(path):
        with open(path) as xml_file:
            return xmltodict.parse(xml_file.read())['dataset']['record']

    @classmethod
    def import_data(cls, path, report_type):
        readers = {
            "csv": cls.read_csv,
            "json": cls.read_json,
            "xml": cls.read_xml
        }

        reports = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate
        }

        file_format = path.split('.')[-1]
        list = readers[file_format](path)
        return reports[report_type](list)
