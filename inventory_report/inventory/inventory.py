import csv
import json
import xml.etree.ElementTree as ET


from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


def read_csv(path):
    with open(path) as file:
        data = csv.DictReader(file)
        result = [row for row in data]
        return result


def read_json(path):
    with open(path) as file:
        data = json.load(file)
        result = [row for row in data]
        return result


def read_xml(path):
    with open(path) as file:
        data = ET.parse(file)
        dataArray = data.getroot()

        result = []
        for element in dataArray:
            elements = {}
            for e in element:
                elements[e.tag] = e.text
            result.append(elements)
        return result


def report_type(type, result):
    if type == "simples":
        return SimpleReport.generate(result)
    if type == "completo":
        return CompleteReport.generate(result)


class Inventory:
    def import_data(path, type):
        if "csv" in path:
            result = read_csv(path)
        if "xml" in path:
            result = read_xml(path)
        if "json" in path:
            result = read_json(path)
        return report_type(type, result)

    pass
