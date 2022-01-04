from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        file_content = cls.read(path)
        if type == "simples":
            return SimpleReport.generate(file_content)
        elif type == "completo":
            return CompleteReport.generate(file_content)

    @classmethod
    def read(cls, path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)
