from datetime import datetime


class FunctionsReport():
    @classmethod
    def order_date(cls, list_prod):
        date_order = {}
        dates = [dates_ant['data_de_fabricacao'] for dates_ant in list_prod]
        for date in dates:
            if not date_order:
                date_order['date_ant'] = date
            date_new = datetime.strptime(date, '%Y-%m-%d')
            date_ant = datetime.strptime(date_order['date_ant'], '%Y-%m-%d')
            if (datetime.now() - date_new) > (datetime.now() - date_ant):
                date_order['date_ant'] = date
        return date_order['date_ant']

    @classmethod
    def nearest_date(cls, list_prod):
        date_nearest = {}
        dates = [dates['data_de_validade'] for dates in list_prod]
        for date in dates:
            if not date_nearest:
                date_nearest['date_val'] = date
            date_new = datetime.strptime(date, '%Y-%m-%d')
            date_val = datetime.strptime(date_nearest['date_val'], '%Y-%m-%d')
            if date_new < datetime.now():
                pass
            elif (date_new - datetime.now()) < (date_val - datetime.now()):
                date_nearest['date_val'] = date
        return date_nearest['date_val']

    @classmethod
    def companies(cls, list_prod):
        companies_big = {}
        companies = [companies['nome_da_empresa'] for companies in list_prod]
        for company in companies:
            if not companies_big.get(company):
                companies_big[company] = 0
            companies_big[company] += 1
        return companies_big


class SimpleReport:
    @classmethod
    def generate(cls, list_prod):
        order = FunctionsReport.order_date(list_prod)
        nearest = FunctionsReport.nearest_date(list_prod)
        company = max(FunctionsReport.companies(list_prod))
        return (
            f'Data de fabricação mais antiga: {order}\n'
            f'Data de validade mais próxima: {nearest}\n'
            f'Empresa com maior quantidade de produtos estocados: {company}\n'
        )
