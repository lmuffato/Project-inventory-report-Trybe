from inventory_report.reports.check_date import CheckDate
from statistics import mode


class SimpleReport:
    @classmethod
    def generate(cls, data):
        fabrication_dates = [row["data_de_fabricacao"] for row in data]
        oldest_fabrication = CheckDate.filter_oldest(fabrication_dates)

        expiration_dates = [row["data_de_validade"] for row in data]
        closer_expiration = CheckDate.filter_closest(expiration_dates)

        companies_list = [row["nome_da_empresa"] for row in data]
        greatest_company = cls.__filter_company(companies_list)

        return (f"Data de fabricação mais antiga: {oldest_fabrication}\n"
                f"Data de validade mais próxima: {closer_expiration}\n"
                f"Empresa com maior quantidade de produtos estocados: "
                f"{greatest_company}\n")

    def __filter_company(data):
        most_frequent = mode(data)
        print(most_frequent)
        return most_frequent
