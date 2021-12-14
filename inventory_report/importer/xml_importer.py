from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith("xml"):
            with open(path) as file:
                dict_arr = xmltodict.parse(file)
            return dict_arr
        else:
            raise ValueError("Arquivo inválido")
