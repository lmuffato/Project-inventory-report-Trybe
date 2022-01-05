from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(stock):
        stored_fabrication_date = []
        stored_validation_date = []
        today_date = datetime.today().strftime('%Y-%m-%d')
        enterprise_name = []
        for product in stock:
            stored_fabrication_date.append(product['data_de_fabricacao'])
            if product['data_de_validade'] > today_date:
                stored_validation_date.append(product['data_de_validade'])
            enterprise_name.append(product['nome_da_empresa'])
        enterprise_count = Counter(enterprise_name)
        formated_string = (
            f"Data de fabricação mais antiga: {min(stored_fabrication_date)}\n"
            f"Data de validade mais próxima: {min(stored_validation_date)}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {max(enterprise_count)}\n"
        )
        return formated_string
