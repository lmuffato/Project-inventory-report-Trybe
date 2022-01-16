class SimpleReport:
    def generate(arr):
        manufacturing = [date["data_de_fabricacao"] for date in arr]
        expiration = [date["data_de_validade"] for date in arr]
        list_company = [stock["nome_da_empresa"] for stock in arr]
        name_company = ''

        for company in list_company:
            bigger_stock = 0
            if list_company.count(company) > bigger_stock:
                bigger_stock = list_company.count(company)
                name_company = company

        sentence1 = f"Data de fabricação mais antiga: {min(manufacturing)}"
        sentence2 = f"Data de validade mais próxima: {min(expiration)}"
        sentence3 = "Empresa com maior quantidade de produtos estocados: "

        return f"{sentence1}\n{sentence2}\n{sentence3}{name_company}"
