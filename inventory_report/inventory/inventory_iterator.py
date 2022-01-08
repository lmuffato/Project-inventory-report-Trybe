from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, products):
        self.products = products
        self.current_product_index = 0

    def __next__(self):
        product = self.products[self.current_product_index]

        if not product:
            raise StopIteration()

        self.current_product_index += 1
        return product
