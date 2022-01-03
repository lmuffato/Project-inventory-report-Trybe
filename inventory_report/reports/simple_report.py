from datetime import datetime
from statistics import mode


class SimpleReport():

    def generate(data):
        curr_date = datetime.now().strftime('%Y-%m-%d"')

        expiration_date_arr = [prod['data_de_validade'] for prod in data
                               if prod['data_de_validade'] > curr_date]

        manufactoring_date_arr = [prod['data_de_fabricacao'] for prod in data]

        industries = [prod['nome_da_empresa'] for prod in data]

        most_stocked_prods_industry = mode(industries)

        return (
            f'Data de fabricação mais antiga: {min(manufactoring_date_arr)}\n'
            f'Data de validade mais próxima: {min(expiration_date_arr)}\n'
            'Empresa com maior quantidade de produtos estocados: '
            f'{most_stocked_prods_industry}\n'
        )

# Ajuda para f-strings https://pythonacademy.com.br/blog/f-strings-no-python
