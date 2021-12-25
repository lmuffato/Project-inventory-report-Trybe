from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(inventory):
        date_now = datetime.now().strftime("%Y%M%D")
        all_companies = [item["nome_da_empresa"] for item in inventory]
        oldest_manufactured_date = min(
            [item["data_de_fabricacao"] for item in inventory]
        )
        closest_expiration_date = min(
            [
                item["data_de_validade"]
                for item in inventory
                if item["data_de_validade"] > date_now
            ]
        )

        companie_with_more_stock, _quantity = Counter(
            all_companies
        ).most_common(1)[0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufactured_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{companie_with_more_stock}\n"
        )
