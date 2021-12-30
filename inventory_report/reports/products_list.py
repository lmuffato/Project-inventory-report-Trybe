from datetime import datetime


class ProductsList:
    def __init__(self, products):
        self.products = products

    def get_oldest_manufacture_date(self):
        manufacture_dates = [
            datetime.strptime(
                p['data_de_fabricacao'], '%Y-%m-%d'
            ) for p in self.products
        ]

        return datetime.strftime(min(manufacture_dates), '%Y-%m-%d')

    def get_latest_expired_date(self):
        today = datetime.now()

        non_expired_products = [
            p for p in self.products
            if datetime.strptime(p['data_de_validade'], '%Y-%m-%d') > today
        ]

        expired_dates = [
            datetime.strptime(
                p['data_de_validade'], '%Y-%m-%d'
            ) for p in non_expired_products
        ]

        return datetime.strftime(min(expired_dates), '%Y-%m-%d')

    def get_stock_qty_by_company(self):
        company_stock = {}
        for p in self.products:
            if p['nome_da_empresa'] in company_stock.keys():
                company_stock[p['nome_da_empresa']] += 1
            else:
                company_stock[p['nome_da_empresa']] = 1

        return company_stock

    def get_company_with_largest_stock(self):
        stock_by_company = self.get_stock_qty_by_company()

        return max(stock_by_company, key=stock_by_company.get)
