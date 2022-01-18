from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = list()

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, report):
        response = self.importer.import_data(path)
        self.data.extend(response)
        if "simples" in report:
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)
