# class SalesReport(ABC):
# def __init__(self, export_file):
#     self.export_file = export_file
#  ....
# class SalesReportJSON(SalesReport)
# sintaxe: # class MinhaClasseHerdeira(ClasseAscendente)

# classe abstrata: classe que não pode ser instanciada
# método abstrato: método que não pode ser chamado diretamente

# ex: classe abstrata SalesReport e classes herdeiras
# SalesReportJSON e SalesReportCSV
#   nesse exemplo, a classe SalesReport não faz nada, apenas as específicas
#     que fazem
#   nunca teremos um relatório geral, mas apenas relatórios específicos

# No contexto de Programação Orientada a Objetos
# pense que coisas abstratas são coisas criadas para serem especializadas
# por classes herdeiras!

# @classmethod: ações/métodos no nível do objeto (classe mãe) e não no nível
# da instância
# podemos invocar o método abaixo de @classmethod no nível da classe mãe
# sem instanciar a classe mãe

# o primeiro argumento passado para um método de classe é a própria classe
# por convenção, chamamos de cls

# https://caiocarrara.com.br/blog/python-classmethod-o-que-e-e-quando-usar.html

# referência para o uso do timedate
# https://stackoverflow.com/questions/49554491/
# not-supported-between-instances-of-datetime-date-and-str/49798686

# o Counter de collections retorna o seguinte:
# elementoDaLista: número de vezes q ele aparece
# ex: empresas = ["empresa1", "empresa2", "empresa1", "empresa3"]
#   collections.Counter(empresas) retorna:
#   Counter({'empresa1': 2, 'empresa2': 1, 'empresa3': 1})

# https://www.hackerrank.com/challenges/collections-counter/problem


import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, products):
        cls.products = products

        oldest_manufacturing_date = []
        closest_expiration_date = []
        companies_with_stocked_products = []

        for product in cls.products:

            manufacturing_date = datetime.datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ).date()

            oldest_manufacturing_date.append(manufacturing_date)
            oldest_manufacturing_date.sort()

            expiration_date = datetime.datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date()

            if expiration_date > datetime.date.today():
                closest_expiration_date.append(product["data_de_validade"])
                closest_expiration_date.sort()

            Counter(
                companies_with_stocked_products.append(
                    product["nome_da_empresa"]
                )
            )

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date[0]}\n"
            f"Data de validade mais próxima: {closest_expiration_date[0]}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {max(companies_with_stocked_products)}\n"
        )
