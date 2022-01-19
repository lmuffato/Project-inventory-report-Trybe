from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if(len(sys.argv) != 3):  # os argumentos passados pelo terminal devem ser 3
        return print('Verifique os argumentos', file=sys.stderr)
    print(sys.stderr)
    relatory_type = sys.argv[2]
    file_path = sys.argv[1]

    if (sys.argv[1].endswith('.csv')):
        report = InventoryRefactor(CsvImporter)
        sys.stdout.write(report.import_data(file_path, relatory_type))

    elif (sys.argv[1].endswith('json')):
        report = InventoryRefactor(JsonImporter)
        sys.stdout.write(report.import_data(file_path, relatory_type))

    elif (sys.argv[1].endswith('xml')):
        report = InventoryRefactor(XmlImporter)
        sys.stdout.write(report.import_data(file_path, relatory_type))

# Teste manual

# Executar no terminal
# Teste 01
inventory_report 'inventory_report/data/inventory.csv' 'simples'
# Teste 02
# inventory_report 'inventory_report/data/inventory.json' 'simples'
# Teste 03
# inventory_report 'inventory_report/data/inventory.xml' 'completo'
