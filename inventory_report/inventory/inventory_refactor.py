from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, Importer):
        self.importer = Importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)  # classe importada

    def import_data(self, path, type):
        self.data += self.importer.import_data(path)
        if (type == 'simples'):
            return SimpleReport.generate(self.data)
        elif (type == 'completo'):
            return CompleteReport.generate(self.data)
        else:
            raise ValueError("Invalid option")

# Teste manual

# Test 01 - csv
# from inventory_report.importer.csv_importer import CsvImporter
# instance = InventoryRefactor(CsvImporter)
# print(instance.import_data("inventory_report/data/inventory.csv", "simples"))
# iterator = iter(instance)
# first_item_instance = next(iterator)
# print(first_item_instance)

# Test 02 - json
# from inventory_report.importer.json_importer import JsonImporter
# instance = InventoryRefactor(JsonImporter)
# instance.import_data("inventory_report/data/inventory.json", "simples")
# iterator = iter(instance)
# first_item_instance = next(iterator)
# print(first_item_instance)

# Test 03 - xml
# from inventory_report.importer.xml_importer import XmlImporter
# instance = InventoryRefactor(XmlImporter)
# instance.import_data("inventory_report/data/inventory.xml", "simples")
# iterator = iter(instance)
# first_item_instance = next(iterator)
# print(first_item_instance)
