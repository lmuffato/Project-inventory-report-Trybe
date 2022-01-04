# https://stackoverflow.com/questions/2148119
# /how-to-convert-an-xml-string-to-a-dictionary
# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html

from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as xml_file:
            data = xmltodict.parse(xml_file.read())["dataset"]["record"]
            return [dict(item) for item in data]
