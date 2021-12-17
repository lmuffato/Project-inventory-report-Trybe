from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def create_report(simple_report, products_stock):
        report = '\nProdutos estocados por empresa: \n'
        for product in products_stock:
            report += f'- {product}: {products_stock[product]}\n'
        return simple_report + report

    @classmethod
    def generate(self, list):
        simple_report = SimpleReport.generate(list)
        stock_by_company = SimpleReport.verify_companies_stock(list)
        complete_report = self.create_report(
            simple_report, stock_by_company)
        return complete_report
