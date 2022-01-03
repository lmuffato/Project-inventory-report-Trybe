# from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self) -> InventoryIterator:
        return InventoryIterator(self.data)

    def import_data(self, file_path, report_type="simples"):
        report = SimpleReport if report_type == "simples" else CompleteReport
        self.data += self.importer.import_data(file_path)
        return report.generate(self.data)
