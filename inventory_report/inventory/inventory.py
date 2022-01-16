# https://www.hashtagtreinamentos.com/como-trabalhar-com-arquivos-csv-no-python?gclid=Cj0KCQiA5OuNBhCRARIsACgaiqXIP6Kj1pXLiLT5BSkDQKmPxlAndhWV_Uksba5hWdw3uhdazARVqQYaAimrEALw_wcB
import csv
import json

import xmltodict as xml

from inventory_report.reports.complete_report import CompleteReport as cr
from inventory_report.reports.simple_report import SimpleReport as sr


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith(".csv"):
            with open(path, mode="r") as csv_file:
                reader = csv.DictReader(csv_file)
                data = [row for row in reader]
        if path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
        if path.endswith(".xml"):
            with open(path) as xml_file:
                file = xml.parse(xml_file.read())["dataset"]["record"]
                data = [dict(item) for item in file]
        if type == "simples":
            return sr.generate(data)
        return cr.generate(data)
