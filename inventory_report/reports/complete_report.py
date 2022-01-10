from .simple_report import SimpleReport
import collections


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, product_list):
        nomes_empresa = []
        resultado = "Produtos estocados por empresa: \n"
        reporte_simples = super().generate(product_list)
        for product in product_list:
            nomes_empresa.append(product["nome_da_empresa"])
        empresas_quantidade = collections.Counter(nomes_empresa)
        for empresa, quantidade in empresas_quantidade.items():
            resultado += f"- {empresa}: {quantidade}\n"
        return (
            f"{reporte_simples}\n"
            f"{resultado}")

# Ultimo commit para rodar o avaliador