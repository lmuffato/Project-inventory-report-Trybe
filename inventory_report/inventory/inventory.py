import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


class Inventory:

    # resolução para aprovacao do requisito 3 visto no video
    # https://www.youtube.com/watch?v=DRqEk1ipv5E
    def open_csv(path):
        with open(path, mode="r") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            formated_data = []
            for items in data:
                formated_data.append(items)
            return formated_data

    def open_json(path):
        with open(path, mode="r") as file:
            return json.load(file)

    # https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
    # https://stackoverflow.com/questions/3217487/how-to-get-all-the-info-in-xml-into-dictionary-with-python
    # for visto no repositorio do Luan e Orlando
    def open_xml(path):
        data = ET.parse(path)
        xml_data = data.getroot()
        data = [
            {elem.tag: elem.text for elem in item} for item in xml_data
        ]
        return data

    # necessidade de identificar classmethod e trocar self por cls vista
    # no repositório do Jodiel e no stackoverflow
    # https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes

    @classmethod
    def import_data(cls, path, type):
        data = []
        if path.endswith("csv"):
            data = cls.open_csv(path)
        elif path.endswith("json"):
            data = cls.open_json(path)
        elif path.endswith("xml"):
            data = cls.open_xml(path)
        if type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
