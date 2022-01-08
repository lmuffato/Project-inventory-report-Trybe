import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        file_extension = path.split(".")[1]
        if file_extension == 'csv':
            with open(path) as file:
                csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
                header, *data = csv_file
                data = [header, *data]
        if file_extension == 'json':
            with open(path) as file:
                data = json.load(file)
        if file_extension == 'xml':
            tree = ET.parse(path)
            root = tree.getroot()
            data = [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]
        if type == 'simples':
            return SimpleReport.generate(data)
        if type == 'completo':
            return CompleteReport.generate(data)
