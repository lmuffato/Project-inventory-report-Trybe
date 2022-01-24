from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @classmethod
    def generate(cls, data_list):
        companies = {}
        report_result_str = "Produtos estocados por empresa: \n"

        for product in data_list:
            if product["nome_da_empresa"] in companies:
                companies[product["nome_da_empresa"]] += 1
            else:
                companies[product["nome_da_empresa"]] = 1

        for company, quantity in companies.items():
            report_result_str += f"- {company}: {quantity}\n"

        return (
            f"{SimpleReport.generate(data_list)}\n"
            f"{report_result_str}"
        )
