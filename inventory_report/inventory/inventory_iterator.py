from collections.abc import Iterator
from typing import Any


class InventoryIterator(Iterator):
    def __init__(self, collection: Any):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value
