from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type):
        self.data += self.importer.import_data(path)

        if type == 'simples':
            return SimpleReport.generate(self.data)

        if type == 'completo':
            return CompleteReport.generate(self.data)
