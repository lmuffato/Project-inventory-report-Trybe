from datetime import datetime
from collections import Counter
from inventory_report.utils.functions import Functions


class SimpleReport:

    def generate(path):
        today = datetime.today().strftime('%Y-%m-%d')
        older = "3000-01-01"
        validate = "3000-01-01"
        nome = ''
        nomes = []
        older = Functions.data_de_fabricacao(today, path, older)
        validate = Functions.data_de_validade(today, path, validate)
        item = iter(path)
        while item:
            try:
                result = next(item)
                nomes.append(result['nome_da_empresa'])
            except StopIteration:
                break
        nomes = Counter(nomes)
        nome = nomes.most_common()
        nome = nome[0][0]
        return(
            f"Data de fabricação mais antiga: {older}\n"
            f"Data de validade mais próxima: {validate}\n"
            f"Empresa com maior quantidade de produtos estocados: {nome}\n"
        )
