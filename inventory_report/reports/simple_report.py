import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, products):
        cls.products = products

        oldest_manufacturing_date = []
        closest_expiration_date = []
        companies_with_stocked_products = []

        for product in cls.products:

            manufacturing_date = datetime.datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ).date()

            oldest_manufacturing_date.append(manufacturing_date)
            oldest_manufacturing_date.sort()

            expiration_date = datetime.datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date()

            if expiration_date > datetime.date.today():
                closest_expiration_date.append(product["data_de_validade"])
                closest_expiration_date.sort()

            Counter(
                companies_with_stocked_products.append(
                    product["nome_da_empresa"]
                )
            )

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date[0]}\n"
            f"Data de validade mais próxima: {closest_expiration_date[0]}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {max(companies_with_stocked_products)}\n"
        )
