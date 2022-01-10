from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
from ..importer.csv_importer import CsvImporter
from ..importer.xml_importer import XmlImporter
from ..importer.json_importer import JsonImporter


def report_type(type, response):
    if type == "simples":
        return SimpleReport.generate(response)
    if type == "completo":
        return CompleteReport.generate(response)


class Inventory:
    def import_data(path, type):
        if "csv" in path:
            response = CsvImporter.import_data(path)
        elif "xml" in path:
            response = XmlImporter.import_data(path)
        elif "json" in path:
            response = JsonImporter.import_data(path)
        return report_type(type, response)
    pass
