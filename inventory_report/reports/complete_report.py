from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(products):
        simple_report_result = SimpleReport.generate(products)
        stock = [product['nome_da_empresa'] for product in products]
        companies = Counter(stock)

        quantities = '\nProdutos estocados por empresa: \n'

        for company, value in companies.items():
            quantities += f'- {company}: {value}\n'

        return simple_report_result + quantities
