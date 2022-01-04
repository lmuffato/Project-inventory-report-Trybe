import xml.etree.ElementTree as ET
import json
import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    __report_functions = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    def import_data(file, type):
        array = []

        if file.endswith(".csv"):
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile)
                array = [row for row in reader]

        elif file.endswith(".json"):
            with open(file, "r") as file:
                array = json.load(file)

        elif file.endswith(".xml"):
            tree = ET.parse(file)
            root = tree.getroot()
            array = [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]

        else:
            raise ValueError("Arquivo inválido")
        return Inventory.__report_functions[type](array)
