import pandas as pd
from datetime import date


class SimpleReport:

    @staticmethod
    def generate(products):
        df = pd.DataFrame(products)
        data_atual = str(date.today())
        oldest_manufactured_date = df['data_de_fabricacao'].min()
        validate = df['data_de_validade']
        closest_expiration_date = validate[(validate > data_atual)].min()
        companie_more_stock = df['nome_da_empresa'].value_counts().idxmax()

        return (f"Data de fabricação mais antiga: {oldest_manufactured_date}\n"
                f"Data de validade mais próxima: {closest_expiration_date}\n"
                f"Empresa com maior quantidade de produtos estocados: "
                f"{companie_more_stock}\n"
                )
