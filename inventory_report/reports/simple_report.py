from collections import Counter


class SimpleReport(list):
    def generate(list):
        data = "2020-10-10"

        data_mais_antiga = min(
            [product["data_de_fabricacao"] for product in list]
        )

        data_atual = min(
            [
                product["data_de_validade"]
                for product in list
                if product["data_de_validade"] > data
            ]
        )

        empresas = [product["nome_da_empresa"] for product in list]
        nome, __quantidades = Counter(empresas).most_common(1)[0]
        # https://pt.stackoverflow.com/questions/484467/imprimir-qualais-palavras-se-repetem-em-python

        return (
            f"Data de fabricação mais antiga: {data_mais_antiga}\n"
            f"Data de validade mais próxima: {data_atual}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{nome}\n"
        )
