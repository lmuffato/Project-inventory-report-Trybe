from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list):
        simple_report = SimpleReport.generate(list)
        counter = Counter(product['nome_da_empresa'] for product in list)
        counter_report = '\n'.join(
            f'- {company}: {count}' for company, count in counter.items()
        )
        return (
            f'{simple_report}\n'
            f'Produtos estocados por empresa: \n'
            f'{counter_report}\n'
        )


lista = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
        "nome_da_empresa": "Industry 1",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
    },
    {
        "id": 2,
        "nome_do_produto": "GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
        "nome_da_empresa": "Hernanne & Sons",
        "data_de_fabricacao": "2020-12-12",
        "data_de_validade": "2023-11-11",
        "numero_de_serie": "FR48 2002 7680 13D2 3OWP LEBA 015",
        "instrucoes_de_armazenamento": "adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
    },
    {
        "id": 3,
        "nome_do_produto": "THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
        "nome_da_empresa": "Industry 2",
        "data_de_fabricacao": "2019-12-12",
        "data_de_validade": "2024-11-11",
        "numero_de_serie": "CU18 2002 7680 1231 3OWP LEBA 015",
        "instrucoes_de_armazenamento": "interdum mauris non ligula pellentesque ultrices    phasellus"
    }
]

classe = CompleteReport()
print(classe.generate(lista))
