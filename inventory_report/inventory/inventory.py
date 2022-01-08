import os
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, report_type):
        _nome, extensao = os.path.splitext(path)
        report_types = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }
        extension = {
            ".csv": CsvImporter.import_data,
        }
        data = extension[extensao](path)
        result = report_types[report_type](data)
        return result
