import os
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, import_type):
        _, file_type = os.path.splitext(path)
        result_importer = cls.get_importer(file_type)(path)
        result_reporter = cls.get_reporter(import_type)(result_importer)

        return result_reporter

    def get_importer(file_type):
        importers = {
            ".csv": CsvImporter.import_data,
            ".json": JsonImporter.import_data,
            ".xml": XmlImporter.import_data,
        }

        return importers[file_type]

    def get_reporter(import_type):
        reporters = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }

        return reporters[import_type]
