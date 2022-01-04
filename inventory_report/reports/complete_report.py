from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def product_by_company(list):
        count = [product["nome_da_empresa"] for product in list]
        return Counter(count)

    @classmethod
    def generate(cls, list):
        stocked_products = "".join(
            f'- {company_name}: {cls.product_by_company(list)[company_name]}\n'
            for company_name in cls.product_by_company(list)
        )

        return (
            f'{SimpleReport.generate(list)}\n'
            'Produtos estocados por empresa: \n'
            f'{stocked_products}'
        )
