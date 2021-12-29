from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list):
        simplereport = SimpleReport.generate(list)
        companys = []

        for item in list:
            companys.append(item['nome_da_empresa'])

        x = Counter(companys).items()

        product_report = (
            "Produtos estocados por empresa: \n"
        )

        for item in x:
            product_report += f"- {item[0]}: {item[1]}\n"

        return (f"{simplereport}\n{product_report}")
