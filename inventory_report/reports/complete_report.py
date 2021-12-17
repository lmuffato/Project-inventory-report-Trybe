from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():
    def __init__(cls, simple_report=SimpleReport()):
        cls.simple_report = simple_report

    def create_report(cls, simple_report, products_stock):
        report = '\n\nProdutos estocados por empresa:\n'
        for product in products_stock:
            report += f'- {product}: {products_stock[product]} \n'
        return simple_report + report

    def generate(cls, list):
        simple_report = cls.simple_report.generate(list)
        stock_by_company = cls.simple_report.verify_companies_stock(list)
        complete_report = cls.create_report(
            simple_report, stock_by_company)
        return complete_report
