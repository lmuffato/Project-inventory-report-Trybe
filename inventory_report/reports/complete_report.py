from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        simple = SimpleReport.generate(data)

        products = Counter(product["nome_da_empresa"] for product in data)

        def products_stocked_report():
            output = ""
            for name in products:
                output += f"- {name}: {products[name]}\n"
            return output

        return (
            f"{simple}\n"
            "Produtos estocados por empresa: \n"
            f"{products_stocked_report()}"
        )
