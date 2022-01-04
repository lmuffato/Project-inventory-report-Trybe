from inventory_report.reports.simple_report import SimpleReport
# from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        simple_report_data = SimpleReport.generate(data)

        industries_stock = dict()
        for prod in data:
            if prod['nome_da_empresa'] in industries_stock:
                industry_name = prod['nome_da_empresa']
                industries_stock[industry_name] += 1
            else:
                industries_stock.update({prod['nome_da_empresa']: 1})

        industries_stock_report = "".join(
            f'- {industry}: {industries_stock[industry]}\n'
            for industry in industries_stock
        )

        return (
            f'{simple_report_data}\n'
            'Produtos estocados por empresa: \n'
            f'{industries_stock_report}'
        )
