# Simple_report
from datetime import datetime


class SimpleReport:
    def generate(data):
        curr_date = datetime.now().strftime('%Y-%M-%D')
        manufacture_date = [item['data_de_fabricacao'] for item in data]
        expiration_date = [item['data_de_validade'] for item in data
                           if item['data_de_validade'] > curr_date]
        company_inventory = [item['nome_da_empresa'] for item in data]
        return (
          f'Data de fabricação mais antiga: {min(manufacture_date)}\n'
          f'Data de validade mais próxima: {min(expiration_date)}\n'
          f'Empresa com maior quantidade de produtos estocados: '
          f'{max(company_inventory)}\n'
        )

# Referência - utilizamos o repositório de Igson
# e Rafael como base para desenvolvimento.
