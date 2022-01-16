import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if(len(sys.argv) != 3):
        return print('Verifique os argumentos', file=sys.stderr)

    file_type = sys.argv[1].split('.')[-1]
    path = sys.argv[1]
    inventory_type = sys.argv[2]

    if(file_type == 'json'):
        report = InventoryRefactor(JsonImporter)
        sys.stdout.write(report.import_data(path, inventory_type))
    elif(file_type == 'csv'):
        report = InventoryRefactor(CsvImporter)
        sys.stdout.write(report.import_data(path, inventory_type))
    elif(file_type == 'xml'):
        report = InventoryRefactor(XmlImporter)
        sys.stdout.write(report.import_data(path, inventory_type))
