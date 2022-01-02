from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(inventory):
        current_date = datetime.now().strftime("%Y%M%D")
        company_names = [item["nome_da_empresa"] for item in inventory]
        oldest_fac_date = min(
            [item["data_de_fabricacao"] for item in inventory]
        )
        neareast_vali_date = min(
            [
                item["data_de_validade"]
                for item in inventory
                if item["data_de_validade"] > current_date
            ]
        )

        biggest_stock_company, _result = Counter(
            company_names
        ).most_common(1)[0]

        return (
            f"""Data de fabricação mais antiga: {oldest_fac_date}
Data de validade mais próxima: {neareast_vali_date}
Empresa com maior quantidade de produtos estocados: {biggest_stock_company}
"""
        )
