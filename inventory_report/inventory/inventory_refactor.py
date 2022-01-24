from collections.abc import Iterable

from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator

class InventoryRefactor(Iterable):
    data = []
    def __init__(self, Importer):
        self.importer = Importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def generate(self, type, list):
        if type == "simples":
            return SimpleReport.generate(list)
        if type == "completo":
            return CompleteReport.generate(list)

    def import_data(self, path, report_type):
        dic_list = self.importer.import_data(path)
        self.data.extend(dic_list)
        return self.generate(report_type, self.data)
