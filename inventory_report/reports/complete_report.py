# class SalesReport(ABC):
# def __init__(self, export_file):
#     self.export_file = export_file
#  ....
# class SalesReportJSON(SalesReport)
# sintaxe: # class MinhaClasseHerdeira(ClasseAscendente)

# vamos invocar um método de classe (o método generate)
# instanciando a classe SimpleReport
# sintaxe: variável = SimpleReport()
# variável.generate()

# super() para indicar que queremos pegar o generate da classe mãe
# variável companies_stock_items_counter
# retorna no formato nome_da_empresa: quantidade de vezes que o nome aparece
# Counter.items(): fazemos o for com .items() para retornar no formato
# [(nome, quantidade de aparições), (nome, quantidade de aparições)]
# for company_name, stock_quantity in dsadadasd.items()
# sendo company_name correspondente a nome
# sendo stock_quantity correspondente a quantidade de aparições
# (ou quantidade de produtos que essa empresa tem em estoque)

from inventory_report.reports.simple_report import SimpleReport

from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        companies_stock_items = []
        complete_report = (
            simple_report + "\nProdutos estocados por empresa: \n"
        )

        for product in products:
            companies_stock_items.append(product["nome_da_empresa"])

        companies_stock_items = Counter(companies_stock_items)

        for (
            company_name,
            stock_quantity,
        ) in companies_stock_items.items():
            complete_report += f"- {company_name}: {stock_quantity}\n"

        return complete_report
