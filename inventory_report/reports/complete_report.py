from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        simple_report = SimpleReport.generate(data)

        stock_counter = Counter(item['nome_da_empresa'] for item in data)

        stock_report = ''.join(
            f'- {company}: {stock_counter[company]}\n'
            for company in stock_counter
            )

        return (
            f'{simple_report}\n'
            'Produtos estocados por empresa: \n'
            f'{stock_report}'
        )
