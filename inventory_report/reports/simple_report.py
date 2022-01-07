import datetime
import collections


dict = [
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 2,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2018-07-05",
    "data_de_validade": "2022-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 2,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "1988-07-05",
    "data_de_validade": "2021-01-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  }
]


class SimpleReport:
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


# print(SimpleReport.generate(dict))
