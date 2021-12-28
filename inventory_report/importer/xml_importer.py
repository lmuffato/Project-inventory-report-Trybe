import json
import xmltodict
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            xml_dic = xmltodict.parse(file.read())
            xml_json = json.dumps(xml_dic)
            return json.loads(xml_json)['dataset']['record']
