from datetime import datetime
from collections import Counter


class SimpleReport:

    def generate(path):
        hoje = datetime.today().strftime('%Y-%m-%d')
        antigo = ''
        validade = ''
        nome = ''
        nomes = []
        item = iter(path)
        while item:
            try:
                result = next(item)
                nomes.append(result['nome_da_empresa'])
                if (antigo or validade or nome) == '':
                    antigo = result['data_de_fabricacao']
                    validade = result['data_de_validade']
                    nome = result['nome_da_empresa']
                if (antigo > result['data_de_fabricacao']):
                    antigo = result['data_de_fabricacao']
                if (validade > result['data_de_validade']):
                    if hoje < result['data_de_validade']:
                        validade = result['data_de_validade']
            except StopIteration:
                break
        nomes = Counter(nomes)
        nome = nomes.most_common()
        nome = nome[0][0]
        print("Data de fabricação mais antiga:", antigo)
        print("Data de validade mais próxima:", validade)
        print("Empresa com maior quantidade de produtos estocados:", nome)
