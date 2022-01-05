from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(stock):
        initial_report = SimpleReport.generate(stock)
        enterprise_name = []
        for products in stock:
            enterprise_name.append(products['nome_da_empresa'])
        enterprise_count = Counter(enterprise_name)
        keys = list(enterprise_count.keys())
        values = list(enterprise_count.values())
        complete_report = ["\nProdutos estocados por empresa: \n"]
        for enterprise_index in range(len(keys)):
            complete_report.append(
                f"- {keys[enterprise_index]}: {values[enterprise_index]}\n"
            )
        return initial_report + "".join(complete_report)
