from datetime import date


class SimpleReport:
    def generate(list):
        actual_date = date.now().strftime('%Y/%M/%D')

        manufacturing_date = [item['data_de_fabricacao'] for item in list]

        expiration_date = [item['data_de_validade'] for item in list
                           if item['data_de_validade'] > actual_date]

        company_largest_stock = [item['nome_da_empresa'] for item in list]

        return (
            f'Data de fabricação mais antiga: {min(manufacturing_date)}\n'
            f'Data de validade mais próxima: {min(expiration_date)}\n'
            f'Empresa com maior quantidade de produtos estocados: '
            f'{max(company_largest_stock)}\n'
        )
