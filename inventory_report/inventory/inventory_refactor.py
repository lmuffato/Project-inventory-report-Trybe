from pathlib import Path
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(InventoryIterator):
    importer = None
    type = ''

    def __init__(self, importer):
        self.importer = importer()

    def import_data_validation(self, path, type):
        if(type not in ['simples', 'completo']):
            raise 'Must enter [simples, completo]'

        ext = Path(path).suffix
        if(ext not in ['.csv', '.json', '.xml']):
            raise ValueError('Invalid extension')

    def import_data(self, path, type):
        self.import_data_validation(path, type)

        if(type == 'simples'):
            products = self.importer.import_data(path)
            return SimpleReport.generate(products)
        elif (type == 'completo'):
            products = self.importer.import_data(path)
            return CompleteReport.generate(products)
        else:
            raise 'Não deveria ter chegado aqui'

    def __iter__(self):
        return super().__iter__()
