from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, products):
        self._products = products
        self._index = 0

    def __next__(self):
        try:
            product = self._products[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration()
        return product
