# Feito por minha dupla Nathalia Zebral
from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


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
