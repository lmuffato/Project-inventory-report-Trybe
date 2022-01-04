from inventory_report.reports.simple_report import SimpleReport

from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        companies_stock_items = []
        complete_report = (
            simple_report + "\nProdutos estocados por empresa: \n"
        )

        for product in products:
            companies_stock_items.append(product["nome_da_empresa"])

        companies_stock_items = Counter(companies_stock_items)

        for (
            company_name,
            stock_quantity,
        ) in companies_stock_items.items():
            complete_report += f"- {company_name}: {stock_quantity}\n"

        return complete_report
