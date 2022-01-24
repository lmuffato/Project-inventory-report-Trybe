import sys
from inventory_report.inventory.inventory import Inventory
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    params = sys.argv

    if len(params) < 3:
        sys.stderr.write("Verifique os argumentos\n")
        return

    report_path = params[1]
    report_type = params[2]

    importer = Inventory.define_importer_type(report_path)
    report = InventoryRefactor(importer).import_data(report_path, report_type)

    print(report, end="")
