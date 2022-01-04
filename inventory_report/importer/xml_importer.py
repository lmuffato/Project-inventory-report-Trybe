from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(data):
        if data.endswith('.xml'):
            with open(data) as file:
                tree = ET.parse(file)
                root = tree.getroot()
                return [
                    {el.tag: el.text for el in subelem}
                    for subelem in root
                ]
        raise ValueError('Arquivo inválido')

# Referência: https://stackabuse.com/reading-and-writing-xml-files-in-python/
