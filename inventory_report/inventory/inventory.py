from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def generate(type, list):

        if type == "simples":
            return SimpleReport.generate(list)
        if type == "completo":
            return CompleteReport.generate(list)

    @classmethod
    def import_data(cls, path, report_type):
        if path.endswith(".csv"):
            dic_list = CsvImporter.import_data(path)
            return cls.generate(report_type, dic_list)
        if path.endswith(".json"):
            dic_list = JsonImporter.import_data(path)
            return cls.generate(report_type, dic_list)
        if path.endswith(".xml"):
            dic_list = XmlImporter.import_data(path)
            return cls.generate(report_type, dic_list)
