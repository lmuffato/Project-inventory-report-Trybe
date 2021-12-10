from datetime import datetime


class SimpleReport:
    def find_oldest_fabrication_date(list):
        oldest_fabrication_date = ""
        for product in list:
            product_date = datetime.strptime(
                    product["data_de_fabricacao"], "%Y-%m-%d"
                )
            if list[0] == product:
                oldest_fabrication_date = product_date
            elif oldest_fabrication_date > product_date:
                oldest_fabrication_date = product_date
        # print(str(oldest_fabrication_date).split(' ')[0])
        return str(oldest_fabrication_date).split(' ')[0]

    def find_closest_expiration_date(list):
        closest_expiration_date = ""
        today = datetime.strptime(
            str(datetime.now()).split(" ")[0], "%Y-%m-%d"
        )
        for product in list:
            product_date = datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            )
            if list[0] == product:
                closest_expiration_date = product_date
            elif (
                closest_expiration_date > product_date and product_date > today
            ):
                closest_expiration_date = product_date
        return str(closest_expiration_date).split(' ')[0]

    def find_enterprise_name_with_most_stocked_products(list):
        enterprises_list = dict()
        for product in list:
            if len(product["nome_da_empresa"]) != 0:
                if product["nome_da_empresa"] not in enterprises_list:
                    enterprises_list[product["nome_da_empresa"]] = 0
                enterprises_list[product["nome_da_empresa"]] += 1
        return max(enterprises_list)

    @classmethod
    def generate(cls, list):
        fabrication = cls.find_oldest_fabrication_date(list)
        expiration = cls.find_closest_expiration_date(list)
        enterprise = cls.find_enterprise_name_with_most_stocked_products(list)
        sentence_1 = f"Data de fabricação mais antiga: {fabrication}"
        sentence_2 = f"Data de validade mais próxima: {expiration}"
        sentence_3 = (
            f"Empresa com maior quantidade de produtos estocados: {enterprise}"
        )
        return f"{sentence_1}\n{sentence_2}\n{sentence_3}\n"


test_list = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id",
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum",
        "nome_da_empresa": "Newton Laboratories, Inc.",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]

print(SimpleReport.generate(test_list))
