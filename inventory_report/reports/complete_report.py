from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(reports):
        companies = Counter()
        message_report = SimpleReport.generate(reports)

        for report in reports:
            companies[report["nome_da_empresa"]] += 1

        message_complete_report = "".join(
          f"- {name}: {company}\n"
          for name, company in companies.items()
        )

        message = (
          f"{message_report}\n"
          "Produtos estocados por empresa: \n"
          f"{message_complete_report}"
        )

        return message
