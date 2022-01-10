from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
    

    __report_functions = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }


    data = {}

    def import_data(self, file_name, type):
        self.importer.import_data(file_name)
        return InventoryRefactor.__report_functions[type](list)


    def __iter__(self):
        return InventoryIterator(self.data)
