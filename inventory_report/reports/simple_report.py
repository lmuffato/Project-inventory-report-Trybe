from datetime import datetime

class SimpleReport:
  def generate(data):
    today = datetime.now().strftime('%Y-%M-%D')
    manufacture_date = [item['data_de_fabricacao'] for item in data]
    expiration_date = [item['data_de_validade'] for item in data
      if item['data_de_validade'] > today]
    return (
      f'Data de fabricação mais antiga: {min(manufacture_date)}',
      f'Data de validade mais próxima: {min(expiration_date)}',
      f'Empresa com maior quantidade de produtos estocados:'
    )