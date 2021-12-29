import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.simple_report import SimpleReport

from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    _type_ = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    def import_data(path, type):
        if path.endswith(".csv"):
            data = []
            with open(path, mode="r") as files:
                file = csv.DictReader(files)
                data = [row for row in file]

        elif path.endswith(".json"):
            with open(path) as files:
                data = json.load(files)
        # https://qastack.com.br/programming/1912434/how-do-i-parse-xml-in-python
        elif path.endswith(".xml"):
            root = ET.parse(path).getroot()
            data = [{x.tag: x.text for x in y} for y in root.findall("record")]
        return Inventory._type_[type](data)
