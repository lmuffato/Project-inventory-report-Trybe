from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        csv_content = cls.read(path)
        if type == "simples":
            return SimpleReport.generate(csv_content)
        elif type == "completo":
            return CompleteReport.generate(csv_content)

    @classmethod
    def read(cls, path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
