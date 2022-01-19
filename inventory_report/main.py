import sys


from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    path = sys.argv[1]
    report_type = sys.argv[2]
    instance = None

    if path.endswith("csv"):
        instance = InventoryRefactor(CsvImporter)
    elif path.endswith("json"):
        instance = InventoryRefactor(JsonImporter)
    else:
        instance = InventoryRefactor(XmlImporter)

    report = instance.import_data(path, report_type)

    sys.stdout.write(report)