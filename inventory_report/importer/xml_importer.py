import xml.etree.ElementTree as E
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if '.xml' in path:
            with open(path, encoding='utf-8') as file:
                file_data = E.parse(file.read())
                return file_data['dataset']['record']
        raise ValueError('Arquivo inválido')
