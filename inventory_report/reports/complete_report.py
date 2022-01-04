from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self, stock):
        self.generate_complete_report(stock)

    def generate_complete_report(stock):
        company_name_list = []
        key = ''
        stock_count = 0

        simple_report = SimpleReport.generate(stock)
        result = f'- {company_name_list[key]}: {stock_count}\n'

# - Nome da empresa: qty
