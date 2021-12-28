from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        simple_report = super().generate(inventory)
        all_companies = ""

        company_counter = Counter(
          product["nome_da_empresa"] for product in inventory
          )

        for c in company_counter:
            all_companies = all_companies + f'- {c}: {company_counter[c]}\n'

        return (
          f"{simple_report}\n"
          f"Produtos estocados por empresa: \n"
          f"{all_companies}"
        )
