from .importer import Importer
import xmltodict


class XML_Importer(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as xmlFile:
            doc = xmltodict.parse(xmlFile.read())
            return [line for line in doc['dataset']['record']]
