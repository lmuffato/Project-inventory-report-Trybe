import datetime
import collections


class SimpleReport:
    @staticmethod
    def generate(file_dict):
        agora = datetime.date.today()
        fabricacao = agora
        validade_min = file_dict[0]['data_de_validade']
        validade_min_date = datetime.date.fromisoformat(validade_min)
        empresas = []
        for obj in file_dict:
            b = obj['data_de_fabricacao']
            c = datetime.date.fromisoformat(b)
            d = obj['data_de_validade']
            validade_medic = datetime.date.fromisoformat(d)
            empresas.append(obj['nome_da_empresa'])
            if fabricacao > c:
                fabricacao = c
            if validade_medic > agora:
                if validade_medic < validade_min_date:
                    validade_min_date = validade_medic
        empresa_max_stock_qtd = collections.Counter(empresas).most_common(1)
        cpny = empresa_max_stock_qtd[0][0]
        a = f"Data de fabricação mais antiga: {fabricacao}\n"
        b = f'Data de validade mais próxima: {validade_min_date}\n'
        c = f'Empresa com maior quantidade de produtos estocados: {cpny}\n'
        return(a + b + c)
