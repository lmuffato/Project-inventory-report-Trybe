from datetime import datetime

class SimpleReport:
  def generate(data):
    today = datetime.now().strftime('%Y-%M-%D')
    data_de_fabricacao = [item['data_de_fabricacao'] for item in data]
    data_de_validade = [item['data_de_validade'] for item in data
                        if item['data_de_validade'] > today]
    return (
      f'Data de fabricação mais antiga: {min(data_de_fabricacao)}',
      f'Data de validade mais próxima: {min(data_de_validade)}',
      f'Empresa com maior quantidade de produtos estocados:'
    )