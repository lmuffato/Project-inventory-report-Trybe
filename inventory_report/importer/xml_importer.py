import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file):
        path = file.split('.')
        extension = path[-1]
        if (extension != "xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(file)
        root = tree.getroot()
        return [
            {elem.tag: elem.text for elem in record}
            for record in root.findall("record")
        ]
