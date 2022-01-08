from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith("csv"):
            items = CsvImporter.import_csv_file(path)
        elif path.endswith("json"):
            items = JsonImporter.import_json_file(path)
        else:
            items = XmlImporter.import_xml_file(path)

        if type == "simples":
            return SimpleReport.generate(items)
        elif type == "completo":
            return CompleteReport.generate(items)
