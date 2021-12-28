from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import open_csv


class CsvImporter(Importer):

    def import_data(path):
        try:
            data = open_csv(path)
            formated_data = Importer.showData(data)
            return formated_data
        except OSError:
            print("Extensão inválida")
