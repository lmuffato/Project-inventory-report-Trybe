from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_name, type):
        self.data.extend(self.importer.import_data(file_name))
        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)
