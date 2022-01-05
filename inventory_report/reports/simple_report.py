from inventory_report.reports.check_date import CheckDate


class SimpleReport:
    @classmethod
    def generate(cls, data):
        fabrication_dates = cls.__get_fabrication_dates(data)
        oldest_fabrication = CheckDate.filter_oldest(fabrication_dates)

        expiration_dates = cls.__get_expiration_dates(data)
        closer_expiration = CheckDate.filter_closest(expiration_dates)

        # greatest_company = ''
        return (f"Data de fabricação mais antiga: {oldest_fabrication}\n"
                f"Data de validade mais próxima: {closer_expiration}\n"
                f"Empresa com maior quantidade de produtos estocados: ")

    def __get_fabrication_dates(data):
        return [row["data_de_fabricacao"] for row in data]

    def __get_expiration_dates(data):
        return [row["data_de_validade"] for row in data]
