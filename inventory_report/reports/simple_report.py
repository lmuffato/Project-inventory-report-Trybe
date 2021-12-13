from datetime import datetime


class SimpleReport():
    def __init__():
        pass

    def generate(dic_arr):
        today = datetime.today()
        old_manufact_date = dic_arr[0]["data_de_fabricacao"]
        nearest_expiring_date_arr = []
        company_arr = []
        for dic in dic_arr:
            if (dic["data_de_fabricacao"] < old_manufact_date):
                old_manufact_date = dic["data_de_fabricacao"]
            if (
                datetime.strptime(dic["data_de_validade"], "%Y-%m-%d")
                > today
            ):
                nearest_expiring_date_arr.append(dic["data_de_validade"])
            company_arr.append(dic["nome_da_empresa"])
        nearest_expiring_date = min(nearest_expiring_date_arr)
        most_products_company = max(set(company_arr), key=company_arr.count)
        return (f"Data de fabricação mais antiga: {old_manufact_date}\n"
                f"Data de validade mais próxima: {nearest_expiring_date}\n"
                "Empresa com maior quantidade de produtos "
                f"estocados: {most_products_company}\n")
