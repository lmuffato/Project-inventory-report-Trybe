# https://www.horadecodar.com.br/2020/04/28/diferenca-entre-staticmethod-e-classmethod-no-python/
# @staticmethod é uma função que não passa implicitamente nem o objeto e
# nem a classe como parâmetro
# esse método/função estático(a) poderia estar solto no código
# é colocado na classe para fins de organização

# @classmethod é um método que passa a classe como primeiro
# argumento de forma implícita
# normal usado quando quero utilizar o método
# sem instanciar a classe (mas pode ser chamado das duas formas)

# https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
# referência para o dictreader

import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    # @staticmethod
    def import_data(file_to_read):
        if file_to_read.endswith(".csv"):
            with open(file_to_read) as file:
                return list(csv.DictReader(file))
        raise ValueError("Arquivo inválido")
