from functools import reduce
from collections import Counter
from typing import List
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data: List):

        def getProp(name):
            def curried(obj):
                return obj[name]
            return curried

        company_counter = Counter(map(getProp('nome_da_empresa'), data))

        def concat(acc, companyName):
            return acc + f"- {companyName}: {company_counter[companyName]}\n"

        return (
           f"{SimpleReport.generate(data)}\n"
           "Produtos estocados por empresa: \n"
           f"{reduce(concat, company_counter, '')}"
        )
