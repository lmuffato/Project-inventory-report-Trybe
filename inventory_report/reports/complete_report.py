from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, data):
        products = Counter(item["nome_da_empresa"] for item in data)

        def company_stock_report():
            stock = ""
            for name in products:
                stock += f"- {name}: {products[name]}\n"
            return stock

        return (
            f"{SimpleReport.generate(data)}\n"
            "Produtos estocados por empresa: \n"
            f"{company_stock_report()}"
        )
