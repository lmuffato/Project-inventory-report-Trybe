from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, inventory):
        self.inventory = inventory
        self.index = 0

    def __next__(self):
        current = self.inventory[self.index]

        if not current:
            raise StopIteration()

        self.index += 1

        return current