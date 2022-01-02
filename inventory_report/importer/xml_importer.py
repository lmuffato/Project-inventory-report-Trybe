from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith('.xml'):
            with open(path, 'r') as file:
                xml_content = file.read()

                ordered_dict = xmltodict.parse(xml_content)
                data_dict = ordered_dict['dataset']['record']

                return data_dict
        raise ValueError("Arquivo inválido")
