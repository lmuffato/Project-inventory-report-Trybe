from typing import Any, List
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer: Any = importer
        self.data: List[Any] = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_path, counter):
        dataList = self.read(file_path)
        self.data = dataList
        if counter == "simples":
            return SimpleReport.generate(dataList)
        elif counter == "completo":
            return CompleteReport.generate(dataList)

    def read(self, file_path):
        return self.importer.import_data(file_path)
