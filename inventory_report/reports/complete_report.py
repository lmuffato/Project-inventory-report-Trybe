from inventory_report.reports.simple_report import SimpleReport


from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list):
        simple_report_method = super().generate(list)

        companies = Counter(company["nome_da_empresa"] for company in list)

        each_inventory = ""

        for company in companies:
            each_inventory += f"- {company}: {companies[company]}\n"

        return (
            f"{simple_report_method}\n"
            "Produtos estocados por empresa: \n"
            f"{each_inventory}"
        )
