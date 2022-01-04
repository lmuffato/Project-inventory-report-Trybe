import xml.etree.ElementTree as ET
from .importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith('.xml'):
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
        else:
            raise ValueError('Invalid file extension')
