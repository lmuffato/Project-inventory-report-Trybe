from datetime import date
from collections import Counter


class ReportUtils:
    def get_stock_by_current_date(stock, key, closest=True):
        if closest:
            return min(
                ReportUtils.parse_stock(stock, key, True),
                key=lambda x: abs(x - date.today()),
            )

        return max(
            ReportUtils.parse_stock(stock, key, True),
            key=lambda x: abs(x - date.today()),
        )

    def get_most_repeated(stock, key):
        return max(ReportUtils.get_for_each_repeated_times(stock, key))

    def parse_stock(stock, key, isDate=False):
        if isDate:
            return [date.fromisoformat(product[key]) for product in stock]

        return [product[key] for product in stock]

    def get_for_each_repeated_times(stock, key):
        parsed_stock = ReportUtils.parse_stock(stock, key)
        return Counter(parsed_stock)

    def parse_stock_key_value_to_un_list(stock, base_string=""):
        base_string_break_line = f"{base_string}\n"
        parsed = "".join(
            [f"- {key}: {value}\n" for key, value in stock.items()]
        )

        return base_string_break_line + parsed
