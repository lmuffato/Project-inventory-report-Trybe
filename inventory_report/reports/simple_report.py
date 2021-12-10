from datetime import datetime


class SimpleReport:
    def find_date(list, target_date, today="1000-01-01"):
        wanted_date = ""
        now = datetime.strptime(str(today).split(" ")[0], "%Y-%m-%d")
        for product in list:
            product_date = datetime.strptime(product[target_date], "%Y-%m-%d")
            if list[0] == product:
                wanted_date = product_date
            elif wanted_date > product_date and product_date > now:
                wanted_date = product_date
        return str(wanted_date).split(" ")[0]

    def find_enterprise_name_with_most_stocked_products(list):
        enterprises_list = dict()
        for product in list:
            if len(product["nome_da_empresa"]) != 0:
                if product["nome_da_empresa"] not in enterprises_list:
                    enterprises_list[product["nome_da_empresa"]] = 0
                enterprises_list[product["nome_da_empresa"]] += 1
        return max(enterprises_list)

    @classmethod
    def generate(cls, list):
        today = datetime.strptime(
            str(datetime.now()).split(" ")[0], "%Y-%m-%d"
        )

        fabrication = cls.find_date(list, "data_de_fabricacao")
        expiration = cls.find_date(list, "data_de_validade", today)
        enterprise = cls.find_enterprise_name_with_most_stocked_products(list)

        sentence_1 = f"Data de fabricação mais antiga: {fabrication}"
        sentence_2 = f"Data de validade mais próxima: {expiration}"
        sentence_3 = (
            f"Empresa com maior quantidade de produtos estocados: {enterprise}"
        )
        return f"{sentence_1}\n{sentence_2}\n{sentence_3}\n"
