from abc import ABC
from typing import Iterator


class InventoryIterator(Iterator, ABC):
    def __iter__(self):
        return super().__iter__()
