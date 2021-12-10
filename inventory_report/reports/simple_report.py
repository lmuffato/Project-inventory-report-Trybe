from datetime import date
import collections


class SimpleReport():
    @classmethod
    def generate(self, product_list):
      data_atual = date.today().strftime("%Y/%m/%d")
      datas_fabricacao = []
      datas_validade = []
      nomes_empresa = []
      for product in product_list:
          datas_fabricacao.append(product["data_de_fabricacao"])
          if product["data_de_validade"] > data_atual:
              datas_validade.append(product["data_de_validade"])
          nomes_empresa.append(product["nome_da_empresa"])
      datas_fabricacao.sort()
      datas_validade.sort()
      nomes_empresa_counter = collections.Counter(nomes_empresa)
      empresa_maior_quantidade = max(nomes_empresa_counter)
      data_validade_mais_recente = datas_validade[0]
      data_fabricacao_mais_antiga = datas_fabricacao[0]
      return (
        "Data de fabricação mais antiga:"
        f" {data_fabricacao_mais_antiga}\n"
        "Data de validade mais próxima:" 
        f" {data_validade_mais_recente}\n"
        "Empresa com maior quantidade de produtos estocados:" 
        f" {empresa_maior_quantidade}\n"
      )