import xml.etree.ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if ".xml" in path:
            tree = ET.parse(path)
            root = tree.getroot()
            list_from_xml = []
            for item in root.findall("record"):
                item_dict = {}
                for data in item:
                    item_dict.update({data.tag: data.text})
                list_from_xml.append(item_dict)
            return list_from_xml

        raise ValueError("Arquivo inválido")
