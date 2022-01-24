from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def define_importer_type(report_type):
        if report_type.endswith(".csv"):
            return CsvImporter
        if report_type.endswith(".json"):
            return JsonImporter
        if report_type.endswith(".xml"):
            return XmlImporter

    @classmethod
    def import_data(cls, path, report_type):
        list = cls.define_importer_type(path).import_data(path)
        if report_type == "simples":
            return SimpleReport.generate(list)
        if report_type == "completo":
            return CompleteReport.generate(list)
