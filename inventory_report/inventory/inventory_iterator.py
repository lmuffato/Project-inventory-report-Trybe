from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, products):
        self.products = products
        self.current_product_index = 0

    def __next__(self):
        try:
            product = self.products[self.current_product_index]
            self.current_product_index += 1
            return product
        except IndexError:
            raise StopIteration()
