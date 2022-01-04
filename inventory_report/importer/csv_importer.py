from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.csv'):
            return Inventory.verify_extension(path)
        raise ValueError("Arquivo inválido")
