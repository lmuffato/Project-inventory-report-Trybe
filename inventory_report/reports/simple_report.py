import pandas as pd
from datetime import date


class SimpleReport:
    @staticmethod
    def generate(products):
        df = pd.DataFrame(products)
        current_date = str(date.today())
        biggest_fac_date = df['data_de_fabricacao'].min()
        vali_date = df['data_de_validade']
        neareast_vali_date = vali_date[(vali_date > current_date)].min()
        company_names = df['nome_da_empresa'].value_counts().idxmax()

        toReturn = f"""Data de fabricação mais antiga: {biggest_fac_date}
Data de validade mais próxima: {neareast_vali_date}
Empresa com maior quantidade de produtos estocados: {company_names}
"""
        return toReturn
