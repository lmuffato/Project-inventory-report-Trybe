from collections import Counter
from datetime import date


class SimpleReport():
    def generate(lists):
        data_atual = date.today()
        counter = Counter()
        data_mais_antiga_de_fabricacao = min(
             [list['data_de_fabricacao'] for list in lists]
        )

        data_mais_proxima_da_validacao = min(
             [
               list['data_de_validade']
               for list in lists
               if list['data_de_validade'] > date.__str__(data_atual)
             ]
        )

        for list in lists:
            counter[list['nome_da_empresa']] += 1

        message = (
          f"Data de fabricação mais antiga: {data_mais_antiga_de_fabricacao}\n"
          f"Data de validade mais próxima: {data_mais_proxima_da_validacao}\n"
          "Empresa com maior quantidade de produtos estocados: "
          f"{max(counter)}\n"
        )

        return message
