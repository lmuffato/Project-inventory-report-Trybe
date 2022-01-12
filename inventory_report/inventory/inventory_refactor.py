from pathlib import Path
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(InventoryIterator):
    importer = None
    max_index = None
    data = []
    index = 0
    type = ''

    def __init__(self, importer):
        self.importer = importer

    def import_data_validation(self, path, type):
        if type not in ['simples', 'completo']:
            raise 'Must enter [simples, completo]'

        ext = Path(path).suffix
        if ext not in ['.csv', '.json', '.xml']:
            raise ValueError('Invalid extension')

    def import_data(self, path, type):
        self.import_data_validation(path, type)
        out = None

        if type == 'simples':
            products = self.importer.import_data(path)
            self.data = [*self.data, *products]
            out = SimpleReport.generate(products)
        elif type == 'completo':
            products = self.importer.import_data(path)
            self.data = [*self.data, *products]
            out = CompleteReport.generate(products)

        self.max_index = len(self.data) - 1

        return out

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        if self.max_index > self.index:
            out = self.data[self.index]
            self.index += 1
            return out
        else:
            raise StopIteration
