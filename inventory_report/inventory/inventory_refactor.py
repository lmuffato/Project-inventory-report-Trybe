from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_path, report_type):
        data_list = self.importer.import_data(file_path)
        self.data.extend(data_list)

        if report_type == "completo":
            return CompleteReport.generate(data_list)
        else:
            return SimpleReport.generate(data_list)
