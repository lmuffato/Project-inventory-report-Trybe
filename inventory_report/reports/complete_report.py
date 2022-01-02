from collections import Counter

from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = SimpleReport.generate(data)

        companies_counter = Counter(item["nome_da_empresa"] for item in data)

        counter = "".join(
            f"- {company}: {companies_counter[company]}\n"
            for company in companies_counter
          )

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{counter}"
        )
