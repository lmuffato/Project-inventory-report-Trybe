from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.json'):
            return Inventory.verify_extension(path)
        raise ValueError("Arquivo inválido")
