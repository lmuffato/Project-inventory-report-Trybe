import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        not_xml = path.split('.')[-1] != 'xml'

        if not_xml:
            raise ValueError("Arquivo inválido")

        with open(path) as xml_file:
            return xmltodict.parse(xml_file.read())['dataset']['record']
