from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(data):
        manufac_date = []

        expiration_date = []
        date_now = datetime.now().strftime("%Y/%M/%D")

        companies = []

        for element in data:
            if element["data_de_fabricacao"]:
                manufac_date.append(element["data_de_fabricacao"])
            if element["data_de_validade"] > date_now:
                expiration_date.append(element["data_de_validade"])
            if element["nome_da_empresa"]:
                companies.append(element["nome_da_empresa"])

        counter = Counter(companies)
        result = max(counter)
        mg1 = f"Data de fabricação mais antiga: {min(manufac_date)}\n"
        mg2 = f"Data de validade mais próxima: {min(expiration_date)}\n"
        mg3 = f"Empresa com maior quantidade de produtos estocados: {result}\n"

        return mg1 + mg2 + mg3
