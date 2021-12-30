import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    __report_type = {
      "simples": SimpleReport.generate,
      "completo": CompleteReport.generate,
    }

    data_content = []

    def import_data(path, type):
        if path.endswith(".csv"):
            with open(path) as csvfile:
                file = csv.DictReader(csvfile)
                data_content = [row for row in file]

        elif path.endswith(".json"):
            with open(path) as jsonfile:
                data_content = json.load(jsonfile)

        elif path.endswith(".xml"):
            tree = ET.parse(path)
            root = tree.getroot()
            data_content = [
                {cont.tag: cont.text for cont in record}
                for record in root.findall("record")
            ]

        return Inventory.__report_type[type](data_content)


# Checagem com a terminação do arquivo:
# https://www.programiz.com/python-programming/methods/string/endswith

# Leitura de arquivos XML e interação:
# https://docs.python.org/3/library/xml.etree.elementtree.html
# https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
