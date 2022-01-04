import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file_path):
        if file_path.endswith(".xml"):
            tree = ET.parse(file_path)
            root = tree.getroot()
            return [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]
        raise ValueError("Arquivo inválido")


""" soruce ref: https://github.com/tryber/sd-010-a-inventory-report/
pull/23/commits/c2b20f69add778bd4746e199a5d4bdf696c4b1d9 """
