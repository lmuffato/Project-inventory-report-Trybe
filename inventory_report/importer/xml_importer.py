from .importer import Importer
import xml.etree.ElementTree as ElementTree


class XmlImporter(Importer):
    @staticmethod
    def import_data(data):
        if data.endswith('.xml'):
            with open(data) as file:
                tree = ElementTree.parse(file)
                root = tree.getroot()
                return [
                    {elem.tag: elem.text for elem in sub_elem}
                    for sub_elem in root
                ]
        raise ValueError('inválido')
