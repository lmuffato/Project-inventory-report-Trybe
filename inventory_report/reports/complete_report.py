from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    def generate(path):
        first_report = SimpleReport.generate(path)
        counted_products = Counter(product["nome_da_empresa"] for product in path)
        second_report = ""
        for company in counted_products:
            second_report += f"- {company}: {counted_products[company]}\n"
        return(
            f"{first_report}\n"
            f"\n Produtos estocados por empresa:\n"
            f"- {second_report}"
        )
