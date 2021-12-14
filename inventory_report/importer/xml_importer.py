from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith("xml"):
            dic_arr = []
            with open(path) as file:
                tree = ET.parse(file)
                root = tree.getroot()
                for record in root:
                    dic_elem = {}
                    for dic in record:
                        dic_elem = {**dic_elem, dic.tag: dic.text}
                    dic_arr.append(dic_elem)
            return dic_arr
        else:
            raise ValueError("Arquivo inválido")
