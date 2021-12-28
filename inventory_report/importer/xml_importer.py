from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import open_xml


class XmlImporter(Importer):

    def import_data(path):
        try:
            data = open_xml(path)
            formated_data = Importer.showData(data)
            return formated_data
        except OSError:
            print("Extensão inválida")
