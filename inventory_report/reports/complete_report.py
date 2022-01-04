from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        simple_report = SimpleReport.generate(data)

        enterprises = []
        for index in data:
            enterprises.append(index["nome_da_empresa"])

        counter = Counter(enterprises)
        keys = list(counter.keys())
        values = list(counter.values())

        length = len(values)
        i = 0

        messages_array = []
        while i < length:
            messages_array.append(f'- {keys[i]}: {values[i]}\n')
            i += 1

        extended_report = '\nProdutos estocados por empresa: \n'
        return simple_report + extended_report + "".join(messages_array)
