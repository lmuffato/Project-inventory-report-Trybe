from typing import List
from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
import os


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[dict]:
        _arquivo, extensao = os.path.splitext(path)
        if extensao != ".xml":
            raise ValueError("Arquivo inválido")
        file = ET.parse(path)
        root = file.getroot()
        filter = "*"
        dict_list = []
        dict_iten = dict()
        for child in root.iter(filter):
            dict_iten[child.tag] = child.text
            if child.tag == "record":
                del dict_iten["record"]
                dict_list.append(dict_iten.copy())
                dict_iten.clear()
        dict_list.append(dict_iten)
        dict_list.pop(0)
        return dict_list
