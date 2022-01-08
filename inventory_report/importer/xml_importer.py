from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as et


class XmlImporter(Importer):

    def import_data(self, path):
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
