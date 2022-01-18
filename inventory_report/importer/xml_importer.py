from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        file_error = path.split('.')[-1]
        if file_error != 'xml':
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            return xmltodict.parse(file.read())['dataset']['record']
