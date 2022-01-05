import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    # Classifica qual classe chamar de acordo com o tipo passado
    _type_ = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    def import_data(path, type):
        data = []
        # Lendo arquivos do tipo csv
        if path.endswith(".csv"):
            with open(path, mode="r") as files:
                file = csv.DictReader(files)
                data = [row for row in file]
        # Lendo arquivos do tipo json
        elif path.endswith(".json"):
            with open(path) as files:
                data = json.load(files)
        # https://qastack.com.br/programming/1912434/how-do-i-parse-xml-in-python
        # Lendo arquivos do tipo xml
        elif path.endswith(".xml"):
            root = ET.parse(path).getroot()
            data = [{x.tag: x.text for x in y} for y in root.findall("record")]
        print(Inventory._type_[type](data))
        return Inventory._type_[type](data)


#  PARA TESTE
Inventory.import_data("inventory_report/data/inventory.json", "simples")
