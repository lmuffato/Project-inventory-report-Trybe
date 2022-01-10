from collections import Counter


class SimpleReport:
    # should return a string formatted as a report.
    def generate(data):
        data_de_fabricacao = []

        nearest_expiration_date = []
        date_now = '2022-01-8'

        companies = []

        for element in data:
            if element["data_de_fabricacao"]:
                data_de_fabricacao.append(element["data_de_fabricacao"])
            if element["data_de_validade"] > date_now:
                nearest_expiration_date.append(element["data_de_validade"])
            if element["nome_da_empresa"]:
                companies.append(element["nome_da_empresa"])

        counter = Counter(companies)
        result = max(counter)

        messages = [
            f"Data de fabricação mais antiga: {min(data_de_fabricacao)}\n",
            f"Data de validade mais próxima: {min(nearest_expiration_date)}\n",
            f"Empresa com maior quantidade de produtos estocados: {result}\n",
        ]

        return "".join(messages)
