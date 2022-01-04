from inventory_report.importer.importer import Importer
from xmltodict import parse


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.xml'):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            xml = parse(file.read())
            return [dict(element) for element in xml['dataset']['record']]
