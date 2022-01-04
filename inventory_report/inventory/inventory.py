import os
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, type_of_report):
        _arquivo, extensao = os.path.splitext(path)
        report_types = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }
        file_extension = {
            ".csv": CsvImporter.import_data,
            ".json": JsonImporter.import_data,
            ".xml": XmlImporter.import_data,
        }
        data = file_extension[extensao](path)
        result = report_types[type_of_report](data)
        return result
