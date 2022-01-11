from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        with open(path, mode="r") as xml_file:
            if path.endswith(".xml"):
                root = ET.fromstringlist(xml_file, parser=None)
                data = [
                  {it.tag: it.text for it in el} for el in root
                ]
                return data
            else:
                raise ValueError("Arquivo inválido")

# Source (doc.):
# https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.fromstring
