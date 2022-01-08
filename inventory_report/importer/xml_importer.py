import os
from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        _nome, extensao = os.path.splitext(path)
        if extensao != ".xml":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            if 'xml' in path:
                reading = ET.parse(file).getroot()
                data = [
                    {elem.tag: elem.text for elem in child}
                    for child in reading
                ]

                return data

# teste