import xml.etree.ElementTree as ET
# https://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/
# https://docs.python.org/3/library/xml.etree.elementtree.html


class Xml_importer:
    def import_xml(path):
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
