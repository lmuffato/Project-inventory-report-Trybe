from datetime import date
from collections import Counter


class SimpleReport():
    def get_earliest_manufacture_date(stock):
        earliest_manufacture_date = stock[0]["data_de_fabricacao"]
        for product in stock:
            if (
              date.fromisoformat(product["data_de_fabricacao"])
              <
              date.fromisoformat(earliest_manufacture_date)):
                earliest_manufacture_date = product["data_de_fabricacao"]
        return earliest_manufacture_date

    def get_closest_expiration_date(stock):
        closest_expiration_date = stock[0]["data_de_validade"]
        for product in stock:
            if (
              date.today()
              <
              date.fromisoformat(product["data_de_validade"])
              <
              date.fromisoformat(closest_expiration_date)
              ):
                closest_expiration_date = product["data_de_validade"]
        return closest_expiration_date

    def count_quantity_of_products(stock):
        company_name = []
        for product in stock:
            company_name.append(product["nome_da_empresa"])
        counter = Counter(company_name)
        return max(counter)

    @classmethod
    def generate(cls, stock):
        return (
              "Data de fabricação mais antiga: "
              f"{cls.get_earliest_manufacture_date(stock)}\n"
              "Data de validade mais próxima: "
              f"{cls.get_closest_expiration_date(stock)}\n"
              "Empresa com maior quantidade de produtos estocados: "
              f"{cls.count_quantity_of_products(stock)}\n"
          )
