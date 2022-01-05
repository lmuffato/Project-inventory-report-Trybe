from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        with open(path, mode="r"):
            if path.endswith(".xml"):
                root = ET.parse(path).getroot()
                data = [
                  {x.tag: x.text for x in y} for y in root.findall("record")
                ]
                return data
            else:
                raise ValueError("Arquivo inválido")
