import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        with open(path) as file:
            if 'xml' in path:
                reading = ET.parse(file).getroot()
                data = [
                    {elem.tag: elem.text for elem in record}
                    for record in reading
                ]
                return data
            else:
                raise ValueError("Arquivo inválido")
