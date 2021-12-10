from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list):
        simple_report = SimpleReport.generate(list)

        company_list = Counter(prod["nome_da_empresa"] for prod in list)

        stock_report = ""
        for item in company_list:
            stock_report += f"- {item}: {company_list[item]}\n"

        return (
            f"{simple_report}\n\n"
            "Produtos estocados por empresa: \n"
            f"{stock_report}"
        )
