from datetime import date
import collections


class SimpleReport:
    def generate(list):
        manufacture_date = []
        expirate_date = []
        companys = []
        actual_date = date.today()

        for item in list:
            manufacture_date.append(item['data_de_fabricacao'])

            companys.append(item['nome_da_empresa'])

            if date.fromisoformat(item['data_de_validade']) > actual_date:
                expirate_date.append(item['data_de_validade'])

        x = max(collections.Counter((companys)).items())[0]

        return (
            f"Data de fabricação mais antiga: {min(manufacture_date)}\n"
            f"Data de validade mais próxima: {min(expirate_date)}\n"
            f"Empresa com maior quantidade de produtos estocados: {x}\n"
        )
