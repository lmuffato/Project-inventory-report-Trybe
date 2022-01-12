import json
import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


class InventoryRefactor:
    def import_json(path):
        with open(path, mode="r") as file:
            return json.load(file)

    def import_csv(path):
        with open(path, mode="r") as file:
            [*data] = csv.DictReader(file, delimiter=",", quotechar='"')
            return data

    def import_xml(path):
        root = ET.parse(path).getroot()
        return [
            {elem.tag: elem.text for elem in item}
            for item in root
        ]

    @classmethod
    def import_data(cls, path, type):
        list = []
        if path.endswith(".json"):
            list = cls.import_json(path)
        if path.endswith(".csv"):
            list = cls.import_csv(path)
        if path.endswith(".xml"):
            list = cls.import_xml(path)
        if type == "completo":
            return CompleteReport.generate(list)
        return SimpleReport.generate(list)
