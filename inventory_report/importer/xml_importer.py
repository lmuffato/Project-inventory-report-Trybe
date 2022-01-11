# https://docs.python.org/3/library/xml.etree.elementtree.html
from functools import reduce
from xml.etree import ElementTree as xml
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file: str):
        def parse(record):
            return reduce(
                lambda acc, cur: {**acc, cur.tag: cur.text}, record, {})

        if not file.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(file) as xml_file:
            tree = xml.parse(xml_file)
            root = tree.getroot()
            elements = root.findall("record")
            return list(map(parse, elements))

#finish later
