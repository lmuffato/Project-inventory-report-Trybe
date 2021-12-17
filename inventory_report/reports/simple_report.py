from datetime import date


class SimpleReport():

    def earliest_manufact_date(products):
        earliest_manufact_date = ''
        for product in products:
            if earliest_manufact_date == '':
                earliest_manufact_date = product['data_de_fabricacao']
            elif earliest_manufact_date > product['data_de_fabricacao']:
                earliest_manufact_date = product['data_de_fabricacao']
        return earliest_manufact_date

    def closest_expiration_date(products):
        closest_expiration_date = ''
        today = date.today()
        for product in products:
            validate_date = product['data_de_validade']
            if(today.strftime("%Y-%m-%D") > validate_date):
                continue
            elif closest_expiration_date == '':
                closest_expiration_date = validate_date
            elif closest_expiration_date > validate_date:
                closest_expiration_date = validate_date
        return closest_expiration_date

    @classmethod
    def verify_companies_stock(cls, products):
        companies_stock = {}
        for product in products:
            company_name = product['nome_da_empresa']
            if(companies_stock != {}):
                for company in list(companies_stock):
                    if(company == company_name):
                        companies_stock[company] += 1
                    else:
                        companies_stock[company_name] = 1
            else:
                companies_stock[company_name] = 1
        return companies_stock

    def largest_stock(companies_stock):
        company_name = max(companies_stock, key=companies_stock.get)
        return company_name

    @classmethod
    def generate(cls, list):
        earliest_manufact_date = cls.earliest_manufact_date(list)
        closest_expiration_date = cls.closest_expiration_date(list)
        companies_stock = cls.verify_companies_stock(list)
        stock = cls.largest_stock(companies_stock)
        
