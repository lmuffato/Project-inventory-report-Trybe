from datetime import datetime


def find_closest_expiration_date(stock):
    curr_date = datetime.now().strftime('%Y-%m-%d')
    date = [
        product["data_de_validade"]
        for product in stock
        if product["data_de_validade"] >= curr_date
    ]
    date.sort()
    return date[0]


def find_oldest_factory_date(stock):
    factory_date = min(
        product["data_de_fabricacao"] for product in stock
    )
    return factory_date


def find_biggest_company(stock):
    company_stock = max(
        company["nome_da_empresa"] for company in stock
    )
    return company_stock


class SimpleReport:
    @classmethod
    def generate(cls, stock):
        manufacturing_date = find_oldest_factory_date(stock)
        expiration_date = find_closest_expiration_date(stock)
        biggest_stock = find_biggest_company(stock)

        return (
            f"Data de fabricação mais antiga: {manufacturing_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com maior quantidade"
            f" de produtos estocados: {biggest_stock}\n"
        )
