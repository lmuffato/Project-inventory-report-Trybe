from datetime import date
from collections import Counter


class SimpleReport():
    def generate(reports):
        actual_date = date.today()
        closest_date = min(
          [
            report['data_de_validade']
            for report in reports
            if report['data_de_validade'] > date.__str__(actual_date)
          ]
        )
        oldest_date = min([report['data_de_fabricacao'] for report in reports])
        counter = Counter()

        for report in reports:
            counter[report['nome_da_empresa']] += 1

        message_report = (
         f"Data de fabricação mais antiga: {oldest_date}\n"
         f"Data de validade mais próxima: {closest_date}\n"
         "Empresa com maior quantidade de produtos estocados: "
         f"{max(counter)}\n"
        )

        return message_report
