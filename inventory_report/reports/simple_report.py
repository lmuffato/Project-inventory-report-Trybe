from datetime import datetime


class SimpleReport:
    def generate(data):
        today = datetime.now().strftime('%Y-%m-%d')
        manufacture_date = [item['data_de_fabricacao'] for item in data]
        expiration_date = [item['data_de_validade'] for item in data
                           if item['data_de_validade'] > today]
        company_stock = [item['nome_da_empresa'] for item in data]
        return (
          f'Data de fabricação mais antiga: {min(manufacture_date)}\n'
          f'Data de validade mais próxima: {min(expiration_date)}\n'
          f'Empresa com maior quantidade de produtos estocados: '
          f'{max(company_stock)}\n'
        )
