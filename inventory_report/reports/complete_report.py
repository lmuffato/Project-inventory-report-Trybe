from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list):
        simple_report = SimpleReport.generate(list)
        counter = Counter(product['nome_da_empresa'] for product in list)
        counter_report = '\n'.join(
            f'- {company}: {count}' for company, count in counter.items()
        )
        return (
            f'{simple_report}\n'
            f'Produtos estocados por empresa: \n'
            f'{counter_report}\n'
        )
