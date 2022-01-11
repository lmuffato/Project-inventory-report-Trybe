from inventory_report.reports.stock_utils import StockUtils


class SimpleReport(StockUtils):
    @classmethod
    def generate(cls, stock):
        return cls.generate_report(stock)

    def generate_report(stock):
        oldest_date = SimpleReport.get_oldest_manufacture_date(
          stock, 'data_de_fabricacao'
        )
        closest_due_date = SimpleReport.get_closest_due_date(
          stock, 'data_de_validade'
        )
        bigger_ivt = SimpleReport.get_biggest_inventory(
          stock, 'nome_da_empresa'
        )

        report_results = [
          f"Data de fabricação mais antiga: {oldest_date}\n",
          f"Data de validade mais próxima: {closest_due_date}\n",
          f"Empresa com maior quantidade de produtos estocados: {bigger_ivt}\n"
        ]

        return "".join(report_results)


# Source:
# Sobre classmethod
# https://python-reference.readthedocs.io/en/latest/docs/functions/classmethod.html
# https://www.tutorialsteacher.com/python/classmethod-decorator
# Documentação Python
# https://docs.python.org/3/library/functions.html#classmethod
# Sobre herança:
# https://algoritmosempython.com.br/cursos/programacao-python/heranca/
