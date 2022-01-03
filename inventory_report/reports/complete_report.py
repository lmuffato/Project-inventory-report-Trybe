from .simple_report import SimpleReport
from collections import Counter


class CompleteReport():

    def generate(stock):
        simple = SimpleReport.generate(stock)
        list_of_products = []
        for r in stock:
            company_name = r['nome_da_empresa']
            list_of_products.append(company_name)
        company_report = dict(Counter(list_of_products))
        list_of_reports = []
        for c in company_report:
            list_of_reports.append(f"- {c}: {company_report[c]}\n")
        return (
            f"{simple}\n"
            "Produtos estocados por empresa: \n"
            f"{''.join(list_of_reports)}")
