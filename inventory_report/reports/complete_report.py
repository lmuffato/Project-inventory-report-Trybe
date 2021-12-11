from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(lists):
        empresas = Counter()
        simpleMessage = SimpleReport.generate(lists)

        for list in lists:
            empresas[list["nome_da_empresa"]] += 1

        completeMessage = "".join(
            f"- {nome}: {empresa}\n" for nome, empresa in empresas.items()
        )

        finalMessage = (
            f"{simpleMessage}\n"
            "Produtos estocados por empresa: \n"
            f"{completeMessage}"
        )
        return finalMessage
