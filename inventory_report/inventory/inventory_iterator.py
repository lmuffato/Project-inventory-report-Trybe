from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, arr):
        self.arr = arr
        self.corrent = 0

    def __next__(self):
        try:
            element = self.arr[self.corrent]
        except IndexError:
            StopIteration
        else:
            self.corrent += 1
            return element
