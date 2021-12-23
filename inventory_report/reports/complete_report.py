from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def contar_produtos(list):
        counter = Counter(product["nome_da_empresa"] for product in list)
        return counter

    @classmethod
    def generate(cls, list):
        simple_report = SimpleReport.generate(list)

        produtos_por_empre = cls.contar_produtos(list)

        products_stocked_report = "".join(
            f"- {company_name}: {produtos_por_empre[company_name]}\n"
            for company_name in produtos_por_empre
        )

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{products_stocked_report}"
        )