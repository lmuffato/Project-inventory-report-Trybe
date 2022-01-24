from datetime import (datetime, date)


class SimpleReport:
    def generate(arr):
        manufacturing = [data["data_de_fabricacao"] for data in arr]
        expiration = []
        list_company = []
        for data in arr:
            key_data = data["data_de_validade"]
            format_data = datetime.strptime(key_data, '%Y-%m-%d').date()
            if format_data >= date.today():
                expiration.append(data["data_de_validade"])
                list_company.append(data["nome_da_empresa"])

        for company in list_company:
            bigger_stock = 0
            if list_company.count(company) > bigger_stock:
                bigger_stock = list_company.count(company)
                name_company = company

        sentence1 = f"Data de fabricação mais antiga: {min(manufacturing)}"
        sentence2 = f"Data de validade mais próxima: {min(expiration)}"
        sentence3 = "Empresa com maior quantidade de produtos estocados: "

        return f"{sentence1}\n{sentence2}\n{sentence3}{name_company}\n"
