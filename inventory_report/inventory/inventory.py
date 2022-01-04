import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    __report_functions = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    def import_data(file, type):
        list = []

        if file.endswith(".csv"):
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile)
                list = [row for row in reader]

        elif file.endswith(".json"):
            with open(file, "r") as file:
                list = json.load(file)

        elif file.endswith(".xml"):
            tree = ET.parse(file)
            root = tree.getroot()
            list = [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]

        else:
            raise ValueError("Arquivo inválido")
        return Inventory.__report_functions[type](list)
