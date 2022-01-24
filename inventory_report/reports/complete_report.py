from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(products):
        simple_report = SimpleReport.generate(products)
        stock = [product["nome_da_empresa"] for product in products]
        enterprises = Counter(stock)

        string = "\nProdutos estocados por empresa: \n"

        for gokuSsj2, vegetaSsj2 in enterprises.items():
            string += f"- { gokuSsj2 }: { int(vegetaSsj2 // 6) }\n"

        return simple_report + string
