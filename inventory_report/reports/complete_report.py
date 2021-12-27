from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    def generate(path):
        first_report = SimpleReport.generate(path)
        counted_items = Counter(product["nome_da_empresa"] for product in path)
        second_report = ""
        for company in counted_items:
            second_report += f"- {company}: {counted_items[company]}\n"
        return(
            f"{first_report}\n"
            "Produtos estocados por empresa: \n"
            f"{second_report}"
        )
