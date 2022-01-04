from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import os


class Inventory:
    def import_data(path, type):
        file_name, extension = os.path.splitext(path)

        data_type = {
            ".csv": CsvImporter.import_data,
            ".json": JsonImporter.import_data,
            ".xml": XmlImporter.import_data,
        }

        data = data_type[extension](path)

        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)
