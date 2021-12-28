from datetime import date
from collections import Counter

class SimpleReport:
  @classmethod
  def generate(cls, inventory):
    oldest_product = min(
      product["data_de_fabricacao"] for product in inventory
    )

    today = str(date.today())
    nearest_validate_date = min(
      product["data_de_validade"] for product in inventory
      if product["data_de_validade"] >= today
    )

    all_companies_count = Counter(product["nome_da_empresa"] for product in inventory)
    most_frequently_company = max(Counter(all_companies_count))

    return (
      f"Data de fabricação mais antiga: {oldest_product}\n"
      f"Data de validade mais próxima: {nearest_validate_date}\n"
      f"Empresa com maior quantidade de "
      f"produtos estocados: {most_frequently_company}\n"
    )