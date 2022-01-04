from datetime import datetime
# https://qastack.com.br/programming/10624937/convert-datetime-object-to-a-string-of-date-only-in-python
# https://www.kite.com/python/answers/how-to-find-the-most-common-element-in-a-list-in-python#:~:text=Call%20max(iterable%2C%20key),common%20element%20of%20the%20list.


class SimpleReport:
    def generate(list_dict):
        list_products = []
        list_products2 = []
        quantity = []
        current_date = datetime.now().strftime("%Y-%m-%d")
        for product in list_dict:
            if product["data_de_fabricacao"]:
                list_products.append(product["data_de_fabricacao"])
            if product["data_de_validade"] >= current_date:
                list_products2.append(product["data_de_validade"])
            if product["nome_da_empresa"]:
                quantity.append(product["nome_da_empresa"])
        print("teste", max(quantity))

        return (
            f"Data de fabricação mais antiga: {min(list_products)}\n"
            f"Data de validade mais próxima: {min(list_products2)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{max(quantity)}\n"
        )
