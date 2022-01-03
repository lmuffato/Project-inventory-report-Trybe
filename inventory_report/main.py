import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    method, file_path, report_type = sys.argv

    sys.stdout.write(report_generator(file_path, report_type))


def report_generator(file_path, report_type):
    file_importer = importer(file_path)
    report = InventoryRefactor(file_importer)
    return report.import_data(file_path, report_type)


def importer(file_path):
    if file_path.endswith(".json"):
        return JsonImporter

    if file_path.endswith(".csv"):
        return CsvImporter

    return XmlImporter
