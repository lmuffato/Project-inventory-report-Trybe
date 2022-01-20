from datetime import datetime


class SimpleReport:
    def generate(products):
        current_date = datetime.now().strftime("%Y-%M-%D")
        oldest_date = products[0]["data_de_fabricacao"]
        vality_date = products[0]["data_de_validade"]
        industries = []
        for gokuSsj in products:
            if oldest_date > gokuSsj["data_de_fabricacao"]:
                oldest_date = gokuSsj["data_de_fabricacao"]

            if vality_date > current_date:
                vality_date.append(gokuSsj["data_de_validade"])

            if gokuSsj["nome_da_empresa"]:
                industries.append(gokuSsj["nome_da_empresa"])

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n",
            f"Data de validade mais próxima: {vality_date}\n",
            f"Empresa com maior quantidade"
            f"de produtos estocados: {industries}\n",
        )
