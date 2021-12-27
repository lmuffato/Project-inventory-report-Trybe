from datetime import datetime


class SimpleReport:
    def generate(data):
        current_date = datetime.now().strftime("%Y/%M/%D")
        manufacturing_date = []
        expiration_date = []
        company_name = []

        for company in data:
            manufacturing_date.append(company["data_de_fabricacao"])
            company_name.append(company["nome_da_empresa"])
            if current_date < company["data_de_validade"]:
                expiration_date.append(company["data_de_validade"])

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_date)}\n"
            f"Data de validade mais próxima: {min(expiration_date)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{max(company_name)}\n"
        )
