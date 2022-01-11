from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        return cls.generate_complete_report(stock)

    def generate_complete_report(stock):
        total_stock_count = SimpleReport.get_stock_count(
          stock, 'nome_da_empresa'
        )

        total_stock_keys = list(total_stock_count.keys())
        total_stock_values = list(total_stock_count.values())

        total_count = len(total_stock_values)

        detailed_report = SimpleReport.get_stock_count_by_company(
          total_stock_keys, total_stock_values, total_count
        )

        complete_report_message = '\nProdutos estocados por empresa: \n'

        simple_report = SimpleReport.generate(stock)

        return simple_report + complete_report_message + "".join(
          detailed_report
        )

# Source:
# Sobre classmethod
# https://python-reference.readthedocs.io/en/latest/docs/functions/classmethod.html
# Documentação Python
# https://docs.python.org/3/library/functions.html#classmethod
# https://www.tutorialsteacher.com/python/classmethod-decorator
# Sobre herança:
# https://algoritmosempython.com.br/cursos/programacao-python/heranca/
