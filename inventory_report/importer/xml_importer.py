import xml.etree.ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith('.xml'):
            raise ValueError('Invalid file extension')
        else:
            tree = ET.parse(path)
            dataset = tree.getroot()
            data = [
                {
                    el.tag: el.text
                    for el in record
                }
                for record in dataset
            ]
            return data
