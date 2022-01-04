from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, reports):
        oldest_date = cls.find_oldest_manufacturing_date(reports)
        first_date = cls.find_first_validate_date(reports)
        company_more_products = cls.company_with_more_products(reports)
        return f"{oldest_date}\n{first_date}\n{company_more_products}\n"

    def find_oldest_manufacturing_date(reports):
        oldest_manufacturing_date = min(
            reports, key=lambda e: e["data_de_fabricacao"]
        )
        return "Data de fabricação mais antiga: {}".format(
            oldest_manufacturing_date["data_de_fabricacao"]
        )

    def find_first_validate_date(reports):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y/%m/%d")
        valid_dates = [
            date
            for date in reports
            if date["data_de_validade"] > formatted_date
        ]
        validate_date = min(valid_dates, key=lambda e: e["data_de_validade"])
        return "Data de validade mais próxima: {}".format(
            validate_date["data_de_validade"]
        )

    def company_with_more_products(reports):
        array = [report["nome_da_empresa"] for report in reports]
        company_more_products = max(
            array,
            key=array.count
        )
        return "Empresa com maior quantidade de produtos estocados: {}".format(
            company_more_products
        )
