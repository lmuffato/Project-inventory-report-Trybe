from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def leitura(path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        if path.endswith(".json"):
            return JsonImporter.import_data(path)
        if path.endswith(".xml"):
            return XmlImporter.import_data(path)

    def import_data(path, type):
        list = Inventory.leitura(path)
        if type == "simples":
            return SimpleReport.generate(list)

        if type == "completo":
            return CompleteReport.generate(list)
