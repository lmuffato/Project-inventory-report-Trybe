from inventory_report.inventory.inventory import FormatTypes
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.csv'):
            raise ValueError('Arquivo inválido')
<<<<<<< HEAD
        return FormatTypes.type_csv(path)
=======
        return FormatTypes.type_csv(path)
>>>>>>> paulovitorInventoryReport
