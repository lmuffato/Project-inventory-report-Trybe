from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CSV_Importer
from inventory_report.importer.json_importer import JSON_Importer
from inventory_report.importer.xml_importer import XML_Importer
import os


class Inventory:
    def import_data(path, type):
        file_name, extension = os.path.splitext(path)

        data_type = {
            ".csv": CSV_Importer.import_data,
            ".json": JSON_Importer.import_data,
            ".xml": XML_Importer.import_data,
        }

        data = data_type[extension](path)

        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)
