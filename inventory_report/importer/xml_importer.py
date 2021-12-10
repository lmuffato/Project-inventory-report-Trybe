import xml.etree.ElementTree as ET

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith(".xml"):
            with open(path, mode="r") as file:
                tree = ET.parse(file)
                root = tree.getroot()
                data = [
                    {elem.tag: elem.text for elem in record} for record in root
                ]
                return data
        raise ValueError("Arquivo inválido")
