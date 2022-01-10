from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list):
        simple_report = SimpleReport.generate(list)

        stock_counter = Counter(item['nome_da_empresa'] for item in list)

        stock_report = ''.join(
            f'- {company}: {stock_counter[company]}\n'
            for company in stock_counter
            )

        return (
            f'{simple_report}\n'
            'Produtos estocados por empresa: \n'
            f'{stock_report}'
        )
