from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        requisito1 = SimpleReport.generate(data)

        companies = []
        for element in data:
            companies.append(element["nome_da_empresa"])

        counter = Counter(companies)
        chaves = list(counter.keys())
        valores = list(counter.values())

        length = len(valores)
        i = 0

        result = []
        while i < length:
            result.append(f'- {chaves[i]}: {valores[i]}\n')
            i += 1

        extended_report = '\nProdutos estocados por empresa: \n'

        return requisito1 + extended_report + "".join(result)
