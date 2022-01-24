from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, list):
        today_date = datetime.today().strftime("%Y-%m-%d")
        oldest_date = min([date["data_de_fabricacao"] for date in list])
        closest_date_to_expiration = min([
          date["data_de_validade"] for date in list
          if date["data_de_validade"] >= today_date])
        comp_name = max(
          [company['nome_da_empresa'] for company in list])

        return (
          f'Data de fabricação mais antiga: {oldest_date}\n'
          f'Data de validade mais próxima: {closest_date_to_expiration}\n'
          f'Empresa com maior quantidade de produtos estocados: {comp_name}\n')
