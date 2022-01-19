from datetime import datetime


class SimpleReport:
    def find_date_factory(list):
        format_date = datetime.now().strftime('%Y-%m-%d')
        date = [
            product["data_de_validade"]
            for product in list
            if product["data_de_validade"] >= format_date
        ]
        date.sort()
        return date[0]

    def find_data_valid(list):
        return min(product["data_de_fabricacao"] for product in list)

    def find_company_max_amount(list):
        return max(company["nome_da_empresa"] for company in list)

    @classmethod
    def generate(cls, list):
        date_factory = cls.find_data_valid(list)
        date_valid = cls.find_date_factory(list)
        company_max_amount = cls.find_company_max_amount(list)

        return (
            f"Data de fabricação mais antiga: {date_factory}\n"
            f"Data de validade mais próxima: {date_valid}\n"
            f"Empresa com maior quantidade"
            f" de produtos estocados: {company_max_amount}\n"
        )
