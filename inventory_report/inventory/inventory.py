import csv
import json

# import xml.etree.ElementTree as ET

from inventory_report.reports.simple_report import SimpleReport

from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        if path.endswith(".csv"):
            with open(path, mode="r") as files:
                file = csv.DictReader(files)
                data = [row for row in file]
            if type == "simples":
                return SimpleReport.generate(data)
            if type == "completo":
                return CompleteReport.generate(data)

        elif path.endswith(".json"):
            with open(path) as files:
                data = json.load(files)
            if type == "simples":
                return SimpleReport.generate(data)
            if type == "completo":
                return CompleteReport.generate(data)

        # elif path.endswith(".xml"):
        #     tree = ET.parse(path)
        #     root = tree.getroot()
        #     for child in root:
        #         data = [child.tag, child.attrib]
        #     if type == "simples":
        #         return SimpleReport.generate(data)
        #     if type == "completo":
        #         return CompleteReport.generate(data)
