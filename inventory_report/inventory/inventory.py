from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    def readFile(path):
        if path.endswith(".csv"):
            file = CsvImporter.import_data(path)
        if path.endswith(".json"):
            file = JsonImporter.import_data(path)
        if path.endswith(".xml"):
            file = XmlImporter.import_data(path)
        return file

    @classmethod
    def import_data(cls, path, type):
        file = cls.readFile(path)

        if type == "simples":
            report = SimpleReport.generate(file)
        if type == "completo":
            report = CompleteReport.generate(file)
        return report
