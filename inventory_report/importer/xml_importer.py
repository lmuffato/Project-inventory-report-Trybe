

import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if '.xml' in path:
            result = []
            tree = ET.parse(path)
            root = tree.getroot()
            for record in root.findall('record'):
                lines = {}
                for product in record:
                   lines[product.tag] = product.text
                result.append(lines)
            return result
        raise ValueError('Arquivo inválido')
