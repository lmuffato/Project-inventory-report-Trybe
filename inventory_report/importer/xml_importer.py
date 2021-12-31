from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):

    @classmethod
    def import_data(self, path):
        if path.endswith("xml"):
            data = ET.parse(path)
            xml_data = data.getroot()
            data = [
                {elem.tag: elem.text for elem in item} for item in xml_data
            ]
            return data
        else:
            raise ValueError("Arquivo inválido")
