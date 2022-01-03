import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(name):
        if name.endswith(".xml"):
            tree = ET.parse(name)
            root = tree.getroot()
            return [
                {el.tag: el.text for el in record}
                for record in root.findall("record")
            ]
        raise ValueError("Arquivo inválido")
