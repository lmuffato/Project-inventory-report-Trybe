from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, list):
        date = datetime.today().strftime("%Y-%m-%d")

        oldest_date = min(product['data_de_fabricacao'] for product in list)

        validity_date = min(
            product['data_de_validade']
            for product in list
            if product['data_de_validade'] > date
        )

        corp = [product['nome_da_empresa'] for product in list]
        name, __quantity = Counter(corp).most_common(1)[0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {validity_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {name}\n"
        )
