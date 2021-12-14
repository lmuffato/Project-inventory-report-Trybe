import pandas as pd

a = pd.read_csv("./inventory_report/data/inventory.csv")
print(a)

class SimpleReport:

    @staticmethod
    def generate(products):
        return "abc"
