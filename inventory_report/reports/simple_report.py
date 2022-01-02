from datetime import datetime
from statistics import mode


class SimpleReport:
    def generate(data):
        date = datetime.now().strftime('%Y-%m-%d"')

        manufacturing_date = [items['data_de_fabricacao'] for items in data]

        expiration_date = [items['data_de_validade'] for items in data
                           if items['data_de_validade'] > date]

        companies = [items['nome_da_empresa'] for items in data]

        return (
            f'Data de fabricação mais antiga: {min(manufacturing_date)}\n'
            f'Data de validade mais próxima: {min(expiration_date)}\n'
            'Empresa com maior quantidade de produtos estocados: '
            f'{mode(companies)}\n'
        )


# referência: https://docs.python.org/3/library/statistics.html#statistics.mode
