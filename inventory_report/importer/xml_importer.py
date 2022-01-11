
from inventory_report.inventory.inventory import FormatTypes
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        return FormatTypes.type_xml(path)
