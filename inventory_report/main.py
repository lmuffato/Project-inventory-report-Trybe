import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos\n")

    file_path = sys.argv[1]
    report_type = sys.argv[2]

    if file_path.endswith(".csv"):
        report_data = InventoryRefactor(CsvImporter)
        print(report_data.import_data(file_path, report_type), end="")

    if file_path.endswith(".json"):
        report_data = InventoryRefactor(JsonImporter)
        print(report_data.import_data(file_path, report_type), end="")

    if file_path.endswith(".xml"):
        report_data = InventoryRefactor(XmlImporter)
        print(report_data.import_data(file_path, report_type), end="")
