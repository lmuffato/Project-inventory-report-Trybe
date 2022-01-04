from datetime import date
# https://www.programiz.com/python-programming/datetime/current-datetime

class SimpleReport:

    def get_first_fabricated(dict):
        first_fabricated = ''
        for products in dict:
            if first_fabricated == '':
                first_fabricated = products['data_de_fabricacao']
            elif first_fabricated > products['data_de_fabricacao']:
                first_fabricated = products['data_de_fabricacao']
        return first_fabricated

    def get_to_expire(dict):
        today = date.today()
        current_date = today.strftime('%Y-%m-%d')
        expire_date = []
        for product in dict:
            if product['data_de_validade'] > current_date:
                expire_date.append(product['data_de_validade'])
        return min(expire_date)

    def more_products(dict):
        companies = []
        for product in dict:
            companies.append(product['nome_da_empresa'])
        return max(companies)
        # outra forma:
        # companies = [product['nome_da_empresa'] for product in dict]
        # return max(companies)

    @classmethod
    def generate(self, dict):
        fabricated = self.get_first_fabricated(dict)
        expire = self.get_to_expire(dict)
        company = self.more_products(dict)

        return (
            f'Data de fabricação mais antiga: {fabricated}\n'
            f'Data de validade mais próxima: {expire}\n'
            f'Empresa com maior quantidade de produtos estocados: {company}\n'
        )
