# https://www.hashtagtreinamentos.com/como-trabalhar-com-arquivos-csv-no-python?gclid=Cj0KCQiA5OuNBhCRARIsACgaiqXIP6Kj1pXLiLT5BSkDQKmPxlAndhWV_Uksba5hWdw3uhdazARVqQYaAimrEALw_wcB
# https://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith
# https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        data = []
        if path.endswith(".csv"):
            with open(path) as csv_file:
                data = list(csv.DictReader(csv_file))
        elif path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
        elif path.endswith(".xml"):
            with open(path) as xml_file:
                list_file = xmltodict.parse(xml_file.read())["dataset"][
                    "record"
                ]
                data = [dict(order) for order in list_file]
                if type == "simples":
                    return SimpleReport.generate(data)
                else:
                    return CompleteReport.generate(data)
