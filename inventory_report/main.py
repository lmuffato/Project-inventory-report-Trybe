from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    if sys.argv[1].endswith(".csv"):
        json_out = InventoryRefactor(CsvImporter)
        return sys.stdout.write(json_out.import_data(sys.argv[1], sys.argv[2]))

    elif sys.argv[1].endswith(".json"):
        json_out = InventoryRefactor(JsonImporter)
        return sys.stdout.write(json_out.import_data(sys.argv[1], sys.argv[2]))

    elif sys.argv[1].endswith(".xml"):
        json_out = InventoryRefactor(XmlImporter)
        return sys.stdout.write(json_out.import_data(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":

    main()
