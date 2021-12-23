from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    def leitura(caminho):
        if caminho.endswith(".csv"):
            return CsvImporter.import_data(caminho)
        if caminho.endswith(".json"):
            return JsonImporter.import_data(caminho)

    @classmethod
    def import_data(cls, caminho, type):
        list = cls.leitura(caminho)
        if type == "simples":
            return SimpleReport.generate(list)
        if type == "completo":
            return CompleteReport.generate(list)
