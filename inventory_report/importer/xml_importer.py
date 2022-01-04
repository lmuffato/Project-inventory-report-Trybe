#  https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
# para utilizar a lib xmltodict
# instalar com pip install xmltodict

from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    # @staticmethod
    def import_data(file_to_read):
        if file_to_read.endswith(".xml"):
            with open(file_to_read, "r") as file:
                xml_file = file.read()

                xml_to_dict = xmltodict.parse(xml_file)
                xml_dict_accessed_values = xml_to_dict["dataset"]["record"]

                return xml_dict_accessed_values
        raise ValueError("Arquivo inválido")
