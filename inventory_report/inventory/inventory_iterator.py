class InventoryIterator:
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        if self._position < (len(self._collection)):
            result = self._collection[self._position]
            self._position += 1

            return result

        raise StopIteration
