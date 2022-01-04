from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def read_file(caminho):
        if caminho.endswith(".csv"):
            return CsvImporter.import_data(caminho)
        if caminho.endswith(".json"):
            return JsonImporter.import_data(caminho)
        if caminho.endswith(".xml"):
            return XmlImporter.import_data(caminho)

    @classmethod
    def import_data(self, caminho, type):
        list = self.read_file(caminho)
        if type == "simples":
            return SimpleReport.generate(list)
        if type == "completo":
            return CompleteReport.generate(list)
