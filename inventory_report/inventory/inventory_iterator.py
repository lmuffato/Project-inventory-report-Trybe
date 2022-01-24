from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.position = 0

    def __next__(self):
        self.position += 1
        if self.position > len(self.collection):
            raise StopIteration()
        data = self.collection[self.position - 1]
        return data
