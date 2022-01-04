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

    def get_biggest_inventory(stock, str_key):
        list_of_companies = [product[str_key] for product in stock]
        return max(Counter(list_of_companies))
