from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    def return_company_stock_qty(list):
        result = ''

        company_group = [company["nome_da_empresa"] for company in list]
        quant = Counter(company_group)

        for company_group_name in quant:
            result += f"- {company_group_name}: {quant[company_group_name]}\n"

        return f"Produtos estocados por empresa: \n{result}"

    @classmethod
    def generate(cls, list):
        generate_simple_report = SimpleReport.generate(list)
        result = cls.return_company_stock_qty(list)
        return f"{generate_simple_report}\n{result}"
