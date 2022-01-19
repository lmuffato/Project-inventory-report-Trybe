from collections.abc import Iterable


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, report_type):
        inventory_list = self.importer.import_data(path)

        self.data = self.data + inventory_list

        if report_type.lower() == "simples":
            result = SimpleReport.generate(self.data)
            return result
        else:
            result = CompleteReport.generate(self.data)
            return result
