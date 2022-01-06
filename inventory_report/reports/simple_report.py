# from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(data):
        manufac_date = []

        expiration_date = []
        # date_now = datetime.now().strftime("%Y/%M/%D")
        date_now = "2021-12-01"
        print(date_now)
        companies = []

        for element in data:
            if element["data_de_fabricacao"]:
                manufac_date.append(element["data_de_fabricacao"])
            if element["data_de_validade"] > date_now:
                expiration_date.append(element["data_de_validade"])
            if element["nome_da_empresa"]:
                companies.append(element["nome_da_empresa"])
        print(expiration_date)
        counter = Counter(companies)
        result = max(counter)
        return (
            f"Data de fabricação mais antiga: {min(manufac_date)}\n"
            f"Data de validade mais próxima: {min(expiration_date)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{result}\n"
        )


# linha 11 dica do Carlos Sá T10A.
