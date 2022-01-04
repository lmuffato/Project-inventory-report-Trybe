from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import json
import xml.etree.ElementTree as ET
import csv


class Inventory:
    def read_CSV(path):
        with open(path) as file:
            return list(csv.DictReader(file))

    def read_JSON(path):
        with open(path) as file:
            list = json.load(file)
        return list

    def read_XML(path):
        tree = ET.parse(path)
        root = tree.getroot()
        list = []
        for item in root.findall('record'):
            item_dict = {}
            for data in item:
                item_dict.update({data.tag: data.text})
            list.append(item_dict)
        return list

    def check_type(self, path):
        if ".json" in path:
            return self.read_JSON(path)
        if ".xml" in path:
            return self.read_XML(path)
        if ".csv" in path:
            return self.read_CSV(path)
        else:
            breakpoint

    @classmethod
    def import_data(self, path, type):
        list = self.check_type(self, path)

        if type == "completo":
            return CompleteReport.generate(list)
        elif type == "simples":
            return SimpleReport.generate(list)
