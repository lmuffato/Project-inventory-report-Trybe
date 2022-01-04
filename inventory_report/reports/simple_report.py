from collections import Counter
from datetime import datetime


class SimpleReport:
    def generate(data):
        creation_date = []
        expiration_date = []
        date_today = datetime.now().strftime("%Y/%M/%D")
        enterprises = []

        for index in data:
            if index["data_de_fabricacao"]:
                creation_date.append(index["data_de_fabricacao"])
            if index["data_de_validade"] > date_today:
                expiration_date.append(index["data_de_validade"])
            if index["nome_da_empresa"]:
                enterprises.append(index["nome_da_empresa"])

        counter = Counter(enterprises)
        result = max(counter)

        report = [
            f"Data de fabricação mais antiga: {min(creation_date)}\n",
            f"Data de validade mais próxima: {min(expiration_date)}\n",
            f"Empresa com maior quantidade de produtos estocados: {result}\n",
        ]

        return "".join(report)
