from inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, file_name, importer):
        self.importer = importer
        self.file_name = file_name

    data = {}

    def import_data(self):
        return self.importer.import_data(self.file_name)


    def __iter__(self):
        data = InventoryIterator(self.import_data())
        return

