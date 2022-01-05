from inventory_report.reports.report import Report
from inventory_report.reports.check_date import CheckDate


class SimpleReport(Report):
    @classmethod
    def generate(cls, data):
        fabrication_dates = [row["data_de_fabricacao"] for row in data]
        oldest_fabrication = CheckDate.filter_oldest(fabrication_dates)

        expiration_dates = [row["data_de_validade"] for row in data]
        closer_expiration = CheckDate.filter_closest(expiration_dates)

        companies_list = [row["nome_da_empresa"] for row in data]
        greatest_company = cls.filter_company(companies_list)

        return (f"Data de fabricação mais antiga: {oldest_fabrication}\n"
                f"Data de validade mais próxima: {closer_expiration}\n"
                f"Empresa com maior quantidade de produtos estocados: "
                f"{greatest_company}\n")
