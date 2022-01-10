from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, src, type):
        data = cls.read_file(src)
        if type == 'simples':
            return SimpleReport.generate(data)
        if type == 'completo':
            return CompleteReport.generate(data)

    @classmethod
    def read_file(cls, src):
        if src.endswith('.csv'):
            return CsvImporter.import_data(src)
        elif src.endswith('.json'):
            return JsonImporter.import_data(src)
        elif src.endswith('.xml'):
            return XmlImporter.import_data(src)
