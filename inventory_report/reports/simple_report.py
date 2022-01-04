from datetime import datetime

class SimpleReport:
  def generate(data):
    data_de_fabricacao = [item['data_de_fabricacao'] for item in data]
    data_de_validade = 
    return (
      f'Data de fabricação mais antiga: {min(data_de_fabricacao)}',
      f'Data de validade mais próxima:',
      f'Empresa com maior quantidade de produtos estocados:'
    )