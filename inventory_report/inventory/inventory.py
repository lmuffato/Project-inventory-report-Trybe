from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET


class Inventory:
    def read_csv(path, relatory_type):
        with open(path) as file:
            reader = csv.DictReader(file)
            file_read = list(reader)
        if relatory_type == "simples":
            return SimpleReport.generate(file_read)
        elif relatory_type == "completo":
            return CompleteReport.generate(file_read)
        else:
            raise ValueError("Relatório inválido")

    def read_json(path, relatory_type):
        with open(path) as file:
            reader = json.load(file)
            file_read = list(reader)
        if relatory_type == "simples":
            return SimpleReport.generate(file_read)
        elif relatory_type == "completo":
            return CompleteReport.generate(file_read)
        else:
            raise ValueError("Relatório inválido")

    def read_xml(path, relatory_type):
        with open(path) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            file_read = [
              {elem.tag: elem.text for elem in child} for child in root
              ]
        if relatory_type == "simples":
            return SimpleReport.generate(file_read)
        elif relatory_type == "completo":
            return CompleteReport.generate(file_read)
        else:
            raise ValueError("Relatório inválido")

    def import_data(file, relatory_type):
        path = file.split('.')
        extension = path[-1]
        if (extension == "csv"):
            file_read = Inventory.read_csv(file, relatory_type)
        if (extension == "json"):
            file_read = Inventory.read_json(file, relatory_type)
        if (extension == "xml"):
            file_read = Inventory.read_xml(file, relatory_type)
        return file_read
