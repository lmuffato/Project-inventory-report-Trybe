from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, file_path, counter):
        data = cls.read(file_path)
        if counter == 'simples':
            return SimpleReport.generate(data)
        elif counter == 'completo':
            return CompleteReport.generate(data)

    @classmethod
    def read(cls, file_path):
        if '.csv' in file_path:
            return CsvImporter.import_data(file_path)
        elif ".json" in file_path:
            return JsonImporter.import_data(file_path)
        elif ".xml" in file_path:
            return XmlImporter.import_data(file_path)
