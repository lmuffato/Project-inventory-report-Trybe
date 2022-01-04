from datetime import date


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
        companies_products = {
            product["nome_da_empresa"]: 0 for product in stock
        }
        for product in stock:
            companies_products[product["nome_da_empresa"]] += 1
        return companies_products

    @classmethod
    def get_company_with_most_products(cls, stock):
        companies_products = cls.count_quantity_of_products(stock)
        return [
            company_name for company_name in companies_products
            if companies_products[company_name]
            == max(companies_products.values())
        ][0]

    @classmethod
    def generate(cls, stock):
        return (
              "Data de fabricação mais antiga: "
              f"{cls.get_earliest_manufacture_date(stock)}\n"
              "Data de validade mais próxima: "
              f"{cls.get_closest_expiration_date(stock)}\n"
              "Empresa com maior quantidade de produtos estocados: "
              f"{cls.get_company_with_most_products(stock)}\n"
          )
