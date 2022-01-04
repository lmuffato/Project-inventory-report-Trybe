from collections import Counter
# https://www.guru99.com/python-counter-collections-example.html

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        initial_report = SimpleReport.generate(data)

        companies_count = Counter(name["nome_da_empresa"] for name in data)

        count = "".join(
            f"- {company}: {companies_count[company]}\n"
            for company in companies_count
        )

        return (
            f"{initial_report}\n"
            "Produtos estocados por empresa: \n"
            f"{count}"
        )
