from datetime import datetime


class SimpleReport:
    def find_date_factory(list):
        format_date = datetime.now().strftime('%Y-%m-%d')
        date = [
            product["data_de_validade"]
            for product in list
            if product["data_de_validade"] >= format_date
        ]
        date.sort()
        return date[0]

    def find_data_valid(list):
        return min(product["data_de_fabricacao"] for product in list)

    def find_company_max_amount(list):
        return max(company["nome_da_empresa"] for company in list)

    @classmethod
    def generate(cls, list):
        date_factory = cls.find_data_valid(list)
        date_valid = cls.find_date_factory(list)
        company_max_amount = cls.find_company_max_amount(list)

        return (
            f"Data de fabricação mais antiga: {date_factory}\n"
            f"Data de validade mais próxima: {date_valid}\n"
            f"Empresa com maior quantidade"
            f" de produtos estocados: {company_max_amount}\n"
        )


test_list = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2014-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2025-05-31",
        "data_de_validade": "2022-01-17",
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
