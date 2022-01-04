from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, enterprises_list=[]):
        self.__index = 0
        self.enterprises_list = enterprises_list

    def __next__(self):
        value = self.enterprises_list[self.__index]

        if not value:
            raise StopIteration()

        self.__index += 1
        return value
