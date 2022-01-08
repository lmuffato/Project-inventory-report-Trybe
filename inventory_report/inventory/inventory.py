from pathlib import Path
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def import_data(path, type):
        importer = None
        extensions = {
            '.xml': XmlImporter,
            '.json': JsonImporter,
            '.csv': CsvImporter
        }
        if(type not in ['simples', 'completo']):
            raise 'Must enter [simples, completo]'

        try:
            importer = extensions[Path(path).suffix]()
            path = path
        except KeyError:
            raise 'The file must be json, xml or csv'

        if(type == 'simples'):
            products = importer.import_data(path)
            return SimpleReport.generate(products)
        elif (type == 'completo'):
            products = importer.import_data(path)
            return CompleteReport.generate(products)
        else:
            raise 'Não deveria ter chegado aqui'
