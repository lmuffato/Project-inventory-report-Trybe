from inventory_report.reports.products_list import ProductsList


class SimpleReport:
    @classmethod
    def generate(cls, products):
        oldest_manufacture_date = ProductsList(
            products
        ).get_oldest_manufacture_date()
        latest_expired_date = ProductsList(products).get_latest_expired_date()
        company_with_largest_stock = ProductsList(
            products
        ).get_company_with_largest_stock()

        r1 = "Data de fabricação mais antiga: "
        r2 = "Data de validade mais próxima: "
        r3 = "Empresa com maior quantidade de produtos estocados: "

        first_row = "{}{}".format(r1, oldest_manufacture_date)
        second_row = "{}{}".format(r2, latest_expired_date)
        third_row = "{}{}".format(r3, company_with_largest_stock)

        return "{}\n{}\n{}\n".format(first_row, second_row, third_row)
