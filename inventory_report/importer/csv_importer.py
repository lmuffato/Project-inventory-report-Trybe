from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @staticmethod
    def import_data(file):
        relatory_type = "simples"
        path = file.split('.')
        extension = path[-1]
        if (extension != "csv"):
            raise ValueError('Arquivo inválid')
        return Inventory.import_data(file, relatory_type)