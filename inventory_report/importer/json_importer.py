from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import open_json


class JsonImporter(Importer):

    def import_data(path):
        try:
            data = open_json(path)
            formated_data = Importer.showData(data)
            return formated_data
        except OSError:
            print("Extensão inválida")
