from inventory_report.inventory.inventory import FormatTypes
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.json'):
            raise ValueError('Arquivo inválido')
        return FormatTypes.type_json(path)