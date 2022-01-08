from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as et
from pathlib import Path


class XmlImporter(Importer):
    def check_extension(path):
        ext = Path(path).suffix
        if(ext != '.xml'):
            raise ValueError('Arquivo inválido')

    def import_data(path):
        XmlImporter.check_extension(path)

        tree = et.parse(path)
        root = tree.getroot()
        out = []
        for x in root:
            dic = dict()
            for y in x:
                dic[y.tag] = y.text

            out.append(dic)

        return out


# from pprint import pprint

# x = XmlImporter()
# pprint(x.import_data('inventory_report/data/inventory.xml'))
