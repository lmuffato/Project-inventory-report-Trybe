# https://www.hashtagtreinamentos.com/como-trabalhar-com-arquivos-csv-no-python?gclid=Cj0KCQiA5OuNBhCRARIsACgaiqXIP6Kj1pXLiLT5BSkDQKmPxlAndhWV_Uksba5hWdw3uhdazARVqQYaAimrEALw_wcB
# testes ok
import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.complete_report import CompleteReport as cr
from inventory_report.reports.simple_report import SimpleReport as sr


class Inventory:
    __report_functions = {
        "simples": sr.generate,
        "completo": cr.generate,
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
