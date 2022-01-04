from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer=JsonImporter):
        self.importer = importer
        self.enterprises_list = []
        self.data = []

    def import_data(self, pathname, report_type="simples"):
        self.data += self.importer.import_data(pathname)

        if report_type == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
