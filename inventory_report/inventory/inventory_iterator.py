from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterator):
        self.iterator = iterator
        self.iterator_index = 0

    def __next__(self):
        self.iterator_index += 1
        if self.iterator_index > len(self.iterator):
            raise StopIteration()

        return self.iterator[self.iterator_index - 1]
