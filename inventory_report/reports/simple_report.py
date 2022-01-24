from datetime import datetime


class SimpleReport:
    def get_manufacturing_date(data_list):
        return min(
            product["data_de_fabricacao"] for product in data_list
        )

    def get_expiration_date(data_list):
        actual_date = datetime.now().strftime("%Y-%m-%d")
        return min(
            product["data_de_validade"]
            for product in data_list
            if product["data_de_validade"] >= actual_date
        )

    def get_company_with_most_products(data_list):
        return max(
            product["nome_da_empresa"] for product in data_list
        )

    @classmethod
    def generate(cls, data_list):
        manufacturing_date = cls.get_manufacturing_date(data_list)
        expiration_date = cls.get_expiration_date(data_list)
        company = cls.get_company_with_most_products(data_list)

        return (
            f"Data de fabricação mais antiga: {manufacturing_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
