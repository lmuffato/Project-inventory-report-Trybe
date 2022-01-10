from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.xml'):
            return Inventory.verify_extension(path)
        raise ValueError("Arquivo inválido")
