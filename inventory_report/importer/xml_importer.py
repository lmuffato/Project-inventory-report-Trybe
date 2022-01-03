from .importer import Importer
import xmltodict


class XmlImporter(Importer):

    def import_data(path):
        with open(path) as file:
            if('xml' in path):
                doc = xmltodict.parse(file.read())
                data = []
                for r in doc['dataset']['record']:
                    data.append(r)
                return data
            else:
                raise ValueError('Arquivo inválido')
