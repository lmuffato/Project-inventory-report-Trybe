from inventory_report.reports.simple_report import SimpleReport


# https://docs.python.org/pt-br/3/tutorial/datastructures.html
class CompleteReport():
    def get_products_by_company(stock):
        company_name = []
        list_without_duplicates = []
        for product in stock:
            company_name.append(product["nome_da_empresa"])
            list_without_duplicates.append(product["nome_da_empresa"])
        result = "Produtos estocados por empresa: \n"
        for company in list_without_duplicates:
            if company_name.count(company) > 1:
                list_without_duplicates.remove(company)
            result += (
                f"- {company}: "
                f"{company_name.count(company)}\n"
            )
        return result

    @classmethod
    def generate(cls, stock):
        simple_report = SimpleReport.generate(stock)
        result = (
            cls.get_products_by_company(stock)
        )
        return simple_report + "\n" + result
