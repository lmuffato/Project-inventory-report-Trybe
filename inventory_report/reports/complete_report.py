from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(stock):
        simple_report = SimpleReport.generate(stock)
        companys = []

        for company in stock:
            companys.append(company["nome_da_empresa"])

        def companys_reports():
            reports = ""
            company_report = Counter(companys)
            for company in company_report:
                reports += (f"- {company}: {company_report[company]}\n")
            return reports

        return(
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{companys_reports()}"
               )
