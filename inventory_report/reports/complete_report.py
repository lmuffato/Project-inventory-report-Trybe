from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_quantity_of_stocked_products_per_company(list):
        quantities_per_company = dict()
        for value in list:
            if value['nome_da_empresa'] not in quantities_per_company:
                quantities_per_company[value['nome_da_empresa']] = 1
            else:
                quantities_per_company[value['nome_da_empresa']] += 1

        return quantities_per_company

    @classmethod
    def generate(cls, list):
        companies = cls.get_quantity_of_stocked_products_per_company(list)
        complete_report = "Produtos estocados por empresa: \n"

        for company, quantity in companies.items():
            complete_report += f"- {company}: {quantity}\n"

        return (
            f"{super().generate(list)}\n"
            f"{complete_report}"
        )
