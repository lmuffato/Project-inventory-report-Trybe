import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(fileName):
        if not fileName.endswith('xml'):
            raise ValueError("Arquivo inválido")
        xmlFile = open(fileName, 'r')
        rawDict = xmltodict.parse(xmlFile.read())
        return rawDict['dataset']['record']
