import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor

#  consultado  o pr de Nicholas Torres para concluir o exercício

def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos")
    extension = sys.argv[1][-3:]
    path = sys.argv[1]
    report_type = sys.argv[2]

    if "csv" in extension:
        report = InventoryRefactor(CsvImporter)
        print(report.import_data(path, report_type), end="")
    else:
        report = InventoryRefactor(JsonImporter)
        print(report.import_data(path, report_type), end="")
