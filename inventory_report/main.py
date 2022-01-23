import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.json_importer import JsonImporter as jsonimp
from inventory_report.importer.csv_importer import CsvImporter as csvimp
from inventory_report.importer.xml_importer import XmlImporter as xmlimp


def main():
    if(len(sys.argv) != 3):
        print('Verifique os argumentos', file=sys.stderr)

    fileType = sys.argv[1].split('.')[-1]

    if(fileType == 'json'):
        report = InventoryRefactor(jsonimp)
        final_report = report.import_data(sys.argv[1], sys.argv[2])
        sys.stdout.write(final_report)
    elif(fileType == 'csv'):
        report = InventoryRefactor(csvimp)
        final_report = report.import_data(sys.argv[1], sys.argv[2])
        sys.stdout.write(final_report)
    elif(fileType == 'xml'):
        report = InventoryRefactor(xmlimp)
        final_report = report.import_data(sys.argv[1], sys.argv[2])
        sys.stdout.write(final_report)

    pass
