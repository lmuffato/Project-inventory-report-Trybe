import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, _type):
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data

    def import_json(path, _type):
        with open(path, 'r') as file:
            return json.load(file)

    def import_xml(path, _type):
        with open(path, 'r') as file:
            tree = ET.parse(file)
            root = tree.getroot()
            data = [
                {el.tag: el.text for el in record}
                for record in root.findall('record')
            ]
            return data

    @classmethod
    def import_data(cls, path, type):
        list = []
        if path.endswith('.csv'):
            list = cls.import_csv(path, type)
        if path.endswith('.json'):
            list = cls.import_json(path, type)
        if path.endswith('.xml'):
            list = cls.import_xml(path, type)
        if type == 'completo':
            return CompleteReport.generate(list)
        return SimpleReport.generate(list)
