from inventory_report.reports.simple_report import SimpleReport as sr
from collections import Counter as cc


class CompleteReport(sr):
    def generate(data):
        simple_report = sr.generate(data)

        companies = []
        for index in data:
            companies.append(index["nome_da_empresa"])

        counter = cc(companies)
        keys = list(counter.keys())
        values = list(counter.values())

        length = len(values)
        i = 0

        messages_array = []
        while i < length:
            messages_array.append(f'- {keys[i]}: {values[i]}\n')
            i += 1

        complete_report = '\nProdutos estocados por empresa: \n'
        return simple_report + complete_report + "".join(messages_array)
