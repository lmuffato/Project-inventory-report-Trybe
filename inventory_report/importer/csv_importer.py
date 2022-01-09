import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        extension_type = path.split(".")[1]
        if (extension_type == "csv"):
            with open(path, mode="r") as file_reports:
                data_csv = csv.DictReader(file_reports)
                reports = list(
                    report for report in data_csv
                )
                return reports
        else:
            raise ValueError("Arquivo inválido")


# print(CsvImporter.import_data("inventory_report/data/inventory.xml"))