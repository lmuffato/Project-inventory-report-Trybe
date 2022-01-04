from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import Csv_importer
from inventory_report.importer.json_importer import Json_importer
from inventory_report.importer.xml_importer import Xml_importer


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith('csv'):
            products = Csv_importer.import_csv(path)
        elif path.endswith('json'):
            products = Json_importer.import_json(path)
        elif path.endswith('xml'):
            products = Xml_importer.import_xml(path)

        if type == 'simples':
            return SimpleReport.generate(products)
        elif type == 'completo':
            return CompleteReport.generate(products)
