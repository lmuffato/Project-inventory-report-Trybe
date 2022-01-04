from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith('csv'):
            products = CsvImporter.import_data(path)

        elif path.endswith('xml'):
            products = XmlImporter.import_data(path)

        else:
            products = JsonImporter.import_data(path)

        if type == 'simples':
            return SimpleReport.generate(products)
        elif type == 'completo':
            return CompleteReport.generate(products)
