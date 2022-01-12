from collections import Counter
from datetime import datetime


class SimpleReport:
    def generate(data):
        m_date = []

        expiration_date = []
        date_now = str(datetime.today()).split()[0]
        comp = []

        for element in data:
            if element["data_de_fabricacao"]:
                m_date.append(element["data_de_fabricacao"])
            if element["data_de_validade"] > date_now:
                expiration_date.append(element["data_de_validade"])
            if element["nome_da_empresa"]:
                comp.append(element["nome_da_empresa"])

        counter = Counter(comp)
        result = max(counter)

        messages = [
            f"Data de fabricação mais antiga: {min(m_date)}\n",
            f"Data de validade mais próxima: {min(expiration_date)}\n",
            f"Empresa com maior quantidade de produtos estocados: {result}\n",
        ]

        return "".join(messages)
