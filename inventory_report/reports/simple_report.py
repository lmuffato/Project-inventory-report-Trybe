from datetime import datetime


class SimpleReport:
    def generate(data):
        dt = datetime.now().strftime('%Y/%M/%D')

        manufacturing_date = [item['data_de_fabricacao'] for item in data]

        expiration_date = [item['data_de_validade'] for item in data
                           if item['data_de_validade'] > dt]

        company_largest_stock = [item['nome_da_empresa'] for item in data]

        return (
            f'Data de fabricação mais antiga: {min(manufacturing_date)}\n'
            f'Data de validade mais próxima: {min(expiration_date)}\n'
            f'Empresa com maior quantidade de produtos estocados: '
            f'{max(company_largest_stock)}\n'
        )
