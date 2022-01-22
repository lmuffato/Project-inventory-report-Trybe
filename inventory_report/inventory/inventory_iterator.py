from collections.abc import Iterator as it


class InventoryIterator(it):
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def __next__(self):
        try:
            current = self.data[self.pos]
        except IndexError:
            raise StopIteration
        else:
            self.pos += 1
            return current
