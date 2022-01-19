from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products):
        companies = Counter(product["nome_da_empresa"] for product in products)
        company = companies.most_common(1)[0][0]

        oldest_manufacturing_date = min(
            product["data_de_fabricacao"] for product in products
        )

        today_date = datetime.now().date()
        closest_expiration_date = min(
            (product["data_de_validade"] for product in products),
            key=lambda date: abs(
                datetime.strptime(date, '%Y-%m-%d').date() - today_date
            )
        )

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )