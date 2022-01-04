import re
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def get_importer(filepath):
    if re.search(".csv$", filepath):
        return CsvImporter
    elif re.search(".json$", filepath):
        return JsonImporter
    else:
        return XmlImporter


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    filepath = sys.argv[1]
    report_type = sys.argv[-1]
    importer = get_importer(filepath)
    instance = InventoryRefactor(importer)
    data = instance.import_data(filepath, report_type)
    sys.stdout.write(data)
