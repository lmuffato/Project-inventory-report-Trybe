from inventory_report.reports.check_date import CheckDate


class SimpleReport:
    @classmethod
    def generate(cls, data):
        fabrication_dates = cls.__get_fabrication_dates(data)
        print(fabrication_dates) 
        oldest_fabrication = CheckDate.filter_oldest(fabrication_dates)
        # closer_expiration = ''
        # greatest_company = ''
        return (f"Data de fabricação mais antiga: {oldest_fabrication}\n"
                f"Data de validade mais próxima: YYYY-MM-DD\n"
                f"Empresa com maior quantidade de produtos estocados: ")

    def __get_fabrication_dates(data):
        return [row["data_de_fabricacao"] for row in data]
