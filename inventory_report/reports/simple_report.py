import pandas as pd
from datetime import date


class SimpleReport:

    @staticmethod
    def generate(products):
        df = pd.DataFrame(products)
        date_now = str(date.today())
        oldest_fac_date = df['data_de_fabricacao'].min()
        vali_date = df['data_de_validade']
        closest_expire_date = vali_date[(vali_date > date_now)].min()
        company_largest_stock = df['nome_da_empresa'].value_counts().idxmax()

        return (f"Data de fabricação mais antiga: {oldest_fac_date}\n"
                f"Data de validade mais próxima: {closest_expire_date}\n"
                f"Empresa com maior quantidade de produtos estocados: "
                f"{company_largest_stock}\n"
                )
