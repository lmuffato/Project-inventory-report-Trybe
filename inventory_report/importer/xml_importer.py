from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith("xml"):
            root = ET.parse(path).getroot()
            return [
                {elem.tag: elem.text for elem in item} for item in root
            ]
        else:
            raise ValueError("Arquivo inválido")
