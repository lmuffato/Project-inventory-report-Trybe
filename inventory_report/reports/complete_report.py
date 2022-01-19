from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        report_header = super().generate(products)

        companies = [product["nome_da_empresa"] for product in products]

        companies_counter = {}

        for company in companies:
            companies_counter[company] = companies_counter.get(company, 0) + 1

        format_companies = [
           f"- {key}: {value}\n" for key, value in companies_counter.items()
        ]

        report_companies = "".join(format_companies)

        return (
            f"{report_header}\n"
            f"Produtos estocados por empresa: \n"
            f"{report_companies}"
        )
  