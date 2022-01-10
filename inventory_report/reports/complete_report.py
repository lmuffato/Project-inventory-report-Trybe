from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self, stock):
        self.stock = stock

    @classmethod
    def generate(self, stock):
        return self.generate_complete_report(stock)

    def generate_complete_report(stock):
        total_stock_count = SimpleReport.get_stock_count(
          stock, 'nome_da_empresa'
        )

        total_stock_keys = list(total_stock_count.keys())
        total_stock_values = list(total_stock_count.values())

        total_count = len(total_stock_values)

        detailed_report = SimpleReport.get_stock_count_by_company(
          total_stock_keys, total_stock_values, total_count
        )

        complete_report_message = '\nProdutos estocados por empresa: \n'

        simple_report = SimpleReport.generate(stock)

        return simple_report + complete_report_message + "".join(
          detailed_report
        )
