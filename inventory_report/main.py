import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos\n")

    path = sys.argv[1]
    report_type = sys.argv[2]

    if path.endswith(".csv"):
        report = InventoryRefactor(CsvImporter)
        print(report.import_data(path, report_type), end="")
    if path.endswith(".json"):
        report = InventoryRefactor(JsonImporter)
        print(report.import_data(path, report_type), end="")
    if path.endswith(".xml"):
        report = InventoryRefactor(XmlImporter)
        print(report.import_data(path, report_type), end="")
