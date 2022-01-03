from datetime import datetime, date


class SimpleReport():

    def find_biggest_stock(list_of_products):
        company = max(set(
            list_of_products),
            key=list_of_products.count
            )
        return company

    def find_oldest_fabrication_date(stock):
        for r in stock:
            if (r == stock[0]):
                oldest_fabrication_date = r['data_de_fabricacao']
            else:
                compared_date = r['data_de_fabricacao']
                if (oldest_fabrication_date > compared_date):
                    oldest_fabrication_date = compared_date
        return oldest_fabrication_date

    def find_nearest_expiration_date(stock):
        for r in stock:
            present = date.today()
            expiration_date = r['data_de_validade']
            date_time = datetime.strptime(expiration_date, "%Y-%m-%d")
            formated_expiration_date = datetime.date(date_time)
            if (formated_expiration_date > present and r == stock[0]):
                nearest_expiration_date = formated_expiration_date
            else:
                if(
                    formated_expiration_date > present and
                    formated_expiration_date < nearest_expiration_date
                ):
                    nearest_expiration_date = formated_expiration_date
        return nearest_expiration_date

    def generate(stock):
        fabrication_date = SimpleReport.find_oldest_fabrication_date(stock)
        expiration_date = SimpleReport.find_nearest_expiration_date(stock)
        list_of_products = []
        for r in stock:
            company_name = r['nome_da_empresa']
            list_of_products.append(company_name)
        company = SimpleReport.find_biggest_stock(list_of_products)
        return (
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n")
