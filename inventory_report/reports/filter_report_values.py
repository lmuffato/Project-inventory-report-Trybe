import statistics
from datetime import date


# https://medium.com/code-85/use-sets-to-count-occurrences-in-python-efec802aa3ad
# https://docs.python.org/pt-br/3.7/howto/sorting.html

class FilterValues:

    def get_data_fabricacao(product_list):
        data_fabricacao = ''
        for product in product_list:
            if data_fabricacao == '':
                data_fabricacao = product['data_de_fabricacao']
            elif product['data_de_fabricacao'] < data_fabricacao:
                data_fabricacao = product['data_de_fabricacao']
        return data_fabricacao

    def get_data_validade(product_list):
        data_validade = ''
        for product in product_list:
            if data_validade == '':
                data_validade = product['data_de_validade']
            elif (data_validade > product['data_de_validade']
                  > date.today().strftime("%Y,%m, %d")):
                data_validade = product['data_de_validade']
        return data_validade

    def get_empresa(product_list):
        empresas = []
        for product in product_list:
            empresas.append(product['nome_da_empresa'])
        empresa = statistics.mode(empresas)
        return empresa

    def get_produtos_por_empresa(product_list):
        empresas = {}
        stringEmpresas = ''
        for product in product_list:
            if product['nome_da_empresa'] not in empresas:
                empresas[product['nome_da_empresa']] = 0
            empresas[product['nome_da_empresa']] += 1
        for empresa in empresas:
            stringEmpresas += f"- {empresa}: {empresas[empresa]}\n"
        return stringEmpresas
