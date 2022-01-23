from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterator):
        self.index = 0
        self.iterator = iterator

    def __next__(self):
        self.index += 1
        if self.index > len(self.iterator):
            raise StopIteration()
        return self.iterator[self.index - 1]
