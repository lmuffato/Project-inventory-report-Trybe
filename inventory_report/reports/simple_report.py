from datetime import date
import collections


class SimpleReport:
    def generate(list):
        manufacture_date = []
        expirate_date = []
        companys = []
        actual_date = date.today()

        for item in list:
            manufacture_date.append(item['data_de_fabricacao'])

            companys.append(item['nome_da_empresa'])

            if date.fromisoformat(item['data_de_validade']) > actual_date:
                expirate_date.append(item['data_de_validade'])

        x = max(collections.Counter((companys)).items())[0]

        return (
            f"Data de fabricação mais antiga: {min(manufacture_date)}\n"
            f"Data de validade mais próxima: {min(expirate_date)}\n"
            f"Empresa com maior quantidade de produtos estocados: {x}"
        )


array = [
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

x = SimpleReport.generate(array)

print(x)
