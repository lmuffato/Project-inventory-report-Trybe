from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(arr):
        name_company = [company["nome_da_empresa"] for company in arr]
        list_stoks = Counter(name_company)
        result = "Produtos estocados por empresa: \n"
        for key, value in list_stoks.items():
            result += f"- {key}: {value}\n"
        simple_report = SimpleReport.generate(arr)

        print(result)

        return f"{simple_report}\n{result}"
