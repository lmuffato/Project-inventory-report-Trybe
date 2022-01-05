import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith(".xml"):
            xmlFile = open(path, 'r')
            data = xmltodict.parse(xmlFile.read())
            return data['dataset']['record']
        raise ValueError("Arquivo inválido")
