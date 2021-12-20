import pandas as pd
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        df = pd.DataFrame(products)
        simple_report = SimpleReport.generate(products)
        complete_report = f"""{simple_report}
Produtos estocados por empresa: \n"""
        company_names = df['nome_da_empresa'].value_counts(sort=False)
        companies_tuples = company_names.iteritems()

        for company in companies_tuples:
            complete_report += f"- {company[0]}: {company[1]}\n"

        return complete_report
