from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import pandas as pd
import xml.etree.ElementTree as ET


class Inventory:
    def readFile(path):
        if path.endswith(".csv"):
            file = pd.read_csv(path).to_dict(orient="records")

        if path.endswith(".json"):
            file = pd.read_json(path).to_dict(orient="records")

        if path.endswith(".xml"):
            with open(path, mode="r") as file:
                tree = ET.parse(file)
                root = tree.getroot()
                print(root)
                data = [
                    {elem.tag: elem.text for elem in child} for child in root
                ]
            return data
        return file

    @classmethod
    def import_data(cls, path, type):
        file = cls.readFile(path)

        if type == "simples":
            report = SimpleReport.generate(file)
        if type == "completo":
            report = CompleteReport.generate(file)
        return report

# problemas com o Panda
