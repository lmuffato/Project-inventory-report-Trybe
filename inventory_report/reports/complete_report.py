from inventory_report.reports.simple_report import SimpleReport


# https://docs.python.org/pt-br/3/tutorial/datastructures.html
class CompleteReport:
    def get_products_by_company(stock):
        company_name = [product["nome_da_empresa"] for product in stock]
        list_without_duplicates = []
        result = "Produtos estocados por empresa: \n"

        for prod in company_name:
            if prod not in list_without_duplicates:
                list_without_duplicates.append(prod)

        for company in list_without_duplicates:
            result += f"- {company}: " f"{company_name.count(company)}\n"

        return result

    @classmethod
    def generate(cls, stock):
        simple_report = SimpleReport.generate(stock)
        result = cls.get_products_by_company(stock)
        return simple_report + "\n" + result
