import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(import_file):
        with open(import_file, "r") as file:
            if not import_file.endswith(".xml"):
                raise ValueError("Arquivo inválido")

            tree = ET.parse(file)
            root = tree.getroot()
            result_data = [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]
            return result_data
