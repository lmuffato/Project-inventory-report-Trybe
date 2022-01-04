import xml.etree.ElementTree as ET
# https://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/
# https://docs.python.org/3/library/xml.etree.elementtree.html
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith('xml'):
            raise ValueError('Arquivo inválido')
        result = []
        tree = ET.parse(path)
        root = tree.getroot()
        for record in root.findall('record'):
            lines = {}
            for product in record:
                lines[product.tag] = product.text
            result.append(lines)
        print(result)
        return result
