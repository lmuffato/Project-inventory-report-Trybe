import xml.etree.ElementTree as ET

from inventory_report.importer.importer import Importer

# import pandas as pd

# list = "../data/inventory.xml"


class XmlImporter(Importer):
    """
    AttributeError:
        'xml.etree.ElementTree.Element' object has no attribute 'getroot
    '"""

    # def read_file(list):
    #     try:
    #         tree = ET.fromstring(open(list).read())
    #         root = tree.getroot()
    #         teste1 = []
    #         teste2 = {}
    #         for item in root:
    #             for record in item:
    #                 teste2[record.tag] = record.text
    #             teste1.append(teste2)
    #             teste2 = {}
    #         return teste1

    #     except OSError:
    #         print("arquivo inexistente")

    def read_file(list):
        try:
            with open(list, "r") as file:
                tree = ET.parse(file)
                root = tree.getroot()
                data = [
                    {elem.tag: elem.text for elem in record} for record in root
                ]
                return data
        except OSError:
            print("arquivo inexistente")

    @classmethod
    def import_data(self, path):
        if path.endswith(".xml"):
            return self.read_file(path)
        raise ValueError("Arquivo inválido")

# ReadXml.read_xlm(list)
