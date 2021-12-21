from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


def return_company_stock_qty(stock):
    companies = [
        company["nome_da_empresa"]
        for company in stock
    ]
    report = ''
    stock_qty = Counter(companies)
    for company_name in stock_qty:
        report += f"- {company_name}: {stock_qty[company_name]}\n"
    return f"Produtos estocados por empresa: \n{report}"


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        simple_report = SimpleReport.generate(stock)
        complete_report = return_company_stock_qty(stock)
        return f"{simple_report}\n{complete_report}"
