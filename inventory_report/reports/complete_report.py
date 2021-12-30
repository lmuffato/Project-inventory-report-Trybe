from inventory_report.reports.products_list import ProductsList
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(products):
        simple_report = SimpleReport.generate(products)

        stock_by_companies = ProductsList(products).get_stock_qty_by_company()

        complete_report = simple_report + "\nProdutos estocados por empresa: \n"
        for company in stock_by_companies.keys():
            complete_report += "- {}: {}\n".format(
                company, stock_by_companies[company]
            )

        return complete_report
