from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def import_data(path, report_type):
        importers = {
            "csv": CsvImporter.import_data,
            "json": JsonImporter.import_data,
            "xml": XmlImporter.import_data
        }

        reports = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate
        }

        file_format = path.split('.')[-1]
        list = importers[file_format](path)
        return reports[report_type](list)
