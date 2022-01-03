from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter


class Inventory:
    @classmethod
    def import_data(cls, file_path, counter):
        data = cls.read(file_path)
        if counter == 'simples':
            return SimpleReport.generate(data)
        elif counter == 'completo':
            return CompleteReport.generate(data)

    @classmethod
    def read(cls, file_path):
        if '.csv' in file_path:
            return CsvImporter.import_data(file_path)
