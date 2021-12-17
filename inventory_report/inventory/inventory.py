from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    def read(path):
        indexOfDot = path.find(".") + 1
        firstLetterOfExtention = path[indexOfDot]
        if firstLetterOfExtention == "j":
            return JsonImporter.import_data(path)
        elif firstLetterOfExtention == "c":
            return CsvImporter.import_data(path)

    @classmethod
    def import_data(cls, path, type):
        list = cls.read(path)
        if type == "simples":
            return SimpleReport.generate(list)
        if type == "completo":
            return CompleteReport.generate(list)
