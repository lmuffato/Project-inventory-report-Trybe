from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter


class Inventory():
    def leitura(path):
        if path.endswith('.csv'):
            return CsvImporter.import_data(path)

    def import_data(path, type):
        list = Inventory.leitura(path)
        print(list)
        if type == 'simples':
            return SimpleReport.generate(list)
        
        if type == 'completo':
            return CompleteReport.generate(list)
