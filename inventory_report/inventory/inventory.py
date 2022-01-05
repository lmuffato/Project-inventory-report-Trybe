from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(file: str, report_type: str):
        importer_dict = {
            "json": JsonImporter.import_data,
            "csv": CsvImporter.import_data,
            "xml": XmlImporter.import_data
        }
        report = SimpleReport if report_type == "simples" else CompleteReport
        return report.generate(importer_dict[file.split(".")[1]](file))


""" class Inventory:
    @staticmethod
    def import_data(file: str, report_type: str):
        return SimpleReport.generate(JsonImporter.import_data(file)) """
