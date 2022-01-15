from collections import Counter as cc
# https://realpython.com/python-counter/


class SimpleReport:
    def generate(data):
        created_at = []
        expired_at = []
        today = "2022-01-15"
        companies = []

        for index in data:
            if index["data_de_fabricacao"]:
                created_at.append(index["data_de_fabricacao"])
            if index["data_de_validade"] > today:
                expired_at.append(index["data_de_validade"])
            if index["nome_da_empresa"]:
                companies.append(index["nome_da_empresa"])

        counter_ent = cc(companies)
        result = max(counter_ent)

        report = [
            f"Data de fabricação mais antiga: {min(created_at)}\n",
            f"Data de validade mais próxima: {min(expired_at)}\n",
            f"Empresa com maior quantidade de produtos estocados: {result}\n",
        ]

        return "".join(report)
