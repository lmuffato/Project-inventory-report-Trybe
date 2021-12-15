# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA

# https://www.programiz.com/python-programming/datetime/strftime
from datetime import datetime


class SimpleReport:
    def generate(list):
        arr_of_earliest_date = []
        arr_of_expiration_date = []
        arr_of_product_quantity = []
        date = datetime.now().strftime("%Y/%m/%d")
        print(date)
        for item in list:
            arr_of_earliest_date.append(item["data_de_fabricacao"])
            arr_of_product_quantity.append(item["nome_da_empresa"])
            if(date < item["data_de_validade"]):
                arr_of_expiration_date.append(item["data_de_validade"])

        return (
            f"Data de fabricação mais antiga: {min(arr_of_earliest_date)}\n"
            f"Data de validade mais próxima: {min(arr_of_expiration_date)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{max(arr_of_product_quantity)}\n"
        )
