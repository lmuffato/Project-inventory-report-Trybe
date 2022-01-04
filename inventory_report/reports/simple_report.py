from datetime import datetime


class SimpleReport:
    def generate(list):
        arr_of_earliest_date = min(item["data_de_fabricacao"] for item in list)
        arr_of_product_quantity = max(item["nome_da_empresa"] for item in list)

        today = datetime.today().strftime("%Y-%m-%d")
        arr_of_expiration_date = min(
            item["data_de_validade"]
            for item in list
            if today < item["data_de_validade"]
        )

        return (
            f"Data de fabricação mais antiga: {arr_of_earliest_date}\n"
            f"Data de validade mais próxima: {arr_of_expiration_date}\n"
            f"Empresa com maior quantidade de "
            f"produtos estocados: {arr_of_product_quantity}\n"
        )
