from datetime import date
from collections import Counter


class StockUtils:

    def get_absolute_date(date_obj): return abs(date_obj - date.today())

    def get_date(stock, str_key):
        return [date.fromisoformat(item[str_key]) for item in stock]

    def get_oldest_manufacture_date(stock, str_key):
        return max(
          StockUtils.get_date(stock, str_key),
          key=StockUtils.get_absolute_date
        )

    def get_closest_due_date(stock, str_key):
        return min(
          StockUtils.get_date(stock, str_key),
          key=StockUtils.get_absolute_date
        )

    def get_company_name_list(stock, str_key):
        return [item[str_key] for item in stock]

    def get_stock_count(stock, str_key):
        return Counter(StockUtils.get_company_name_list(stock, str_key))

    def get_stock_count_by_company(keys, values, total_count):
        key = 0
        detailed_report = []
        while key < total_count:
            detailed_report.append(
              f'- {keys[key]}: {values[key]}\n'
            )
            key += 1
        return detailed_report

    def get_biggest_inventory(stock, str_key):
        return max(StockUtils.get_stock_count(stock, str_key))


# Source:
# Funções lambda:
# http://www.dsc.ufcg.edu.br/~pet/jornal/maio2013/materias/tutoriais.html
# https://medium.com/@otaviobn/entendendo-as-funções-lambda-no-python-cbe3c5abb179
# Objeto datetime:
# https://docs.python.org/3/library/datetime.html
# Python built-in methods:
# https://www.tutorialsteacher.com/python/builtin-methods
