from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(inventory):
        simple_report = SimpleReport.generate(inventory)
        all_companies_stock = dict(
            Counter([item["nome_da_empresa"] for item in inventory])
        )
        output = ""
        for item in all_companies_stock:
            output += f"- {item}: {all_companies_stock[item]}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{output}"
        )
