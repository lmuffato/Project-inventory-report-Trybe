from .importer import Importer
import xmltodict
import os


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_name, extension = os.path.splitext(path)

        if extension != ".xml":
            raise ValueError("Arquivo inválido")

        with open(path) as xmlFile:
            doc = xmltodict.parse(xmlFile.read())
            return [line for line in doc['dataset']['record']]
