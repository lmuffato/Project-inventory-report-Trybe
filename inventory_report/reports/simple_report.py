from inventory_report.reports.check_date import CheckDate


class SimpleReport:
    @classmethod
    def generate(cls, data):
        fabrication_dates = cls.__get_fabrication_dates(data)
        oldest_fabrication = CheckDate.filter_oldest(fabrication_dates)
        # closer_expiration = ''
        # greatest_company = ''
        return (f"Data de fabricação mais antiga: ${oldest_fabrication}"
                f"Data de validade mais próxima: YYYY-MM-DD"
                f"Empresa com maior quantidade de produtos estocados: ")

    def __get_fabrication_dates(data):
        return [row["data_de_fabricacao"] for row in data]
