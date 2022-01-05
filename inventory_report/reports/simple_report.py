from datetime import datetime

# teste = [
#         {
#             "id": 1,
#             "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#             "nome_da_empresa": "Forces of Nature",
#             "data_de_fabricacao": "2020-07-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#             "instrucoes_de_armazenamento": "in blandit ultrices enim",
#         },
#         {
#             "id": 2,
#             "nome_do_produto": "sodium ferric gluconate complex",
#             "nome_da_empresa": "sanofi-aventis U.S. LLC",
#             "data_de_fabricacao": "2020-05-31",
#             "data_de_validade": "2023-01-17",
#             "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#             "instrucoes_de_armazenamento": "duis bibendum morbi",
#         },
#         {
#             "id": 3,
#             "nome_do_produto": "Dexamethasone Sodium Phosphate",
#             "nome_da_empresa": "sanofi-aventis U.S. LLC",
#             "data_de_fabricacao": "2019-09-13",
#             "data_de_validade": "2023-02-13",
#             "numero_de_serie": "BA52 2034 8595 7904 7131",
#             "instrucoes_de_armazenamento": "morbi quis tortor id",
#         },
#         {
#             "id": 4,
#             "nome_do_produto": "Uricum acidum, Benzoicum acidum",
#             "nome_da_empresa": "Newton Laboratories",
#             "data_de_fabricacao": "2019-11-08",
#             "data_de_validade": "2019-11-25",
#             "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
#             "instrucoes_de_armazenamento": "velit eu est congue elementum",
#         },
#     ]


class SimpleReport:
    @classmethod
    def generate(cls, reports):
        oldest_date = cls.find_oldest_manufacturing_date(reports)
        first_date = cls.find_first_validate_date(reports)
        company_more_products = cls.company_with_more_products(reports)
        return f"{oldest_date}\n{first_date}\n{company_more_products}\n"

    def find_oldest_manufacturing_date(reports):
        oldest_manufacturing_date = min(
            reports, key=lambda e: e["data_de_fabricacao"]
        )
        return "Data de fabricação mais antiga: {}".format(
            oldest_manufacturing_date["data_de_fabricacao"]
        )

    def find_first_validate_date(reports):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y/%m/%d")
        valid_dates = [
            date
            for date in reports
            if date["data_de_validade"] > formatted_date
        ]
        validate_date = min(valid_dates, key=lambda e: e["data_de_validade"])
        return "Data de validade mais próxima: {}".format(
            validate_date["data_de_validade"]
        )

    def company_with_more_products(reports):
        occurrences_company_names = [
            report["nome_da_empresa"] for report in reports
        ]

        # https://stackoverflow.com/questions/6987285/find-the-item-with-maximum-occurrences-in-a-list

        company_more_products = max(
            occurrences_company_names, key=occurrences_company_names.count
        )
        return "Empresa com maior quantidade de produtos estocados: {}".format(
            company_more_products
        )


# print(SimpleReport.generate(teste))
