from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, stock):
        return self.generate_complete_report(stock)

    def generate_complete_report(stock):
        key = 0
        total_stock_count = SimpleReport.get_stock_count(
          stock, 'nome_da_empresa'
        )

        total_stock_keys = list(total_stock_count.keys())
        total_stock_values = list(total_stock_count.values())

        total_count = len(total_stock_values)

        detailed_report = []

        while key < total_count:
            detailed_report.append(
              f'- {total_stock_keys[key]}: {total_stock_values[key]}\n'
            )
            key += 1

        complete_report_message = '\nProdutos estocados por empresa: \n'

        simple_report = SimpleReport.generate(stock)

        return simple_report + complete_report_message + "".join(
          detailed_report
        )
