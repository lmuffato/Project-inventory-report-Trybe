from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if ".xml" in path:
            tree = ET.parse(path)
            root = tree.getroot()
            list = []
            for item in root.findall('record'):
                item_dict = {}
                for data in item:
                    item_dict.update({data.tag: data.text})
                list.append(item_dict)
            return list
        else:
            raise ValueError('Arquivo inválido')
