from inventory_report.reports.simple_report import SimpleReport
from collections import OrderedDict

# from simple_report import SimpleReport

# teste = [
#     {
#         "id": 1,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2020-07-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "sodium ferric gluconate complex",
#         "nome_da_empresa": "sanofi-aventis U.S. LLC",
#         "data_de_fabricacao": "2020-05-31",
#         "data_de_validade": "2023-01-17",
#         "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#         "instrucoes_de_armazenamento": "duis bibendum morbi",
#     },
#     {
#         "id": 3,
#         "nome_do_produto": "Dexamethasone Sodium Phosphate",
#         "nome_da_empresa": "Newton Laboratories",
#         "data_de_fabricacao": "2019-09-13",
#         "data_de_validade": "2023-02-13",
#         "numero_de_serie": "BA52 2034 8595 7904 7131",
#         "instrucoes_de_armazenamento": "morbi quis tortor id",
#     },
#     {
#         "id": 4,
#         "nome_do_produto": "Uricum acidum, Benzoicum acidum",
#         "nome_da_empresa": "Newton Laboratories",
#         "data_de_fabricacao": "2019-11-08",
#         "data_de_validade": "2019-11-25",
#         "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
#         "instrucoes_de_armazenamento": "velit eu est congue elementum",
#     },
# ]


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, reports):
        oldest_date = cls.find_oldest_manufacturing_date(reports)
        first_date = cls.find_first_validate_date(reports)
        company_more_products = cls.company_with_more_products(reports)
        company_quantity_products = (
            f"Produtos estocados por empresa: \n{cls.quantityProduct(reports)}"
        )
        report = f"{oldest_date}\n{first_date}\n{company_more_products}\n"

        return f"{report}\n{company_quantity_products}\n"

    def quantityProduct(reports):
        occurrences_company_names = [
            report["nome_da_empresa"] for report in reports
        ]

        ocurrences_quantity_products = [
            (company, occurrences_company_names.count(company))
            for company in occurrences_company_names
        ]

        # https://www.youtube.com/watch?v=1T_bxlFIshI

        quantity_products = list(
            OrderedDict.fromkeys(ocurrences_quantity_products)
        )

        format_quantity_products = [
            f"- {product[0]}: {product[1]}" for product in quantity_products
        ]

        # http://devfuria.com.br/python/convertendo-listas/

        return "\n".join(format_quantity_products)


# print(CompleteReport.generate(teste))
