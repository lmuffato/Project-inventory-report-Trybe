from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        data = cls.read_file(path)
        if type == 'simples':
            return SimpleReport.generate(data)
        if type == 'completo':
            return CompleteReport.generate(data)

    @classmethod
    def read_file(cls, path):
        if path.endswith('.csv'):
            return CsvImporter.import_data(path)
