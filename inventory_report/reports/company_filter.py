
class CompanyFilter:
    def more_products(stock):
        empresas = [
          empresa['nome_da_empresa']
          for empresa in stock
        ]
        return max(empresas)  # empresa em que o nome
