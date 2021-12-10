from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    def create_list_of_enteprises_and_quantity_of_their_products(list):
        enterprises_list = dict()
        for product in list:
            if len(product["nome_da_empresa"]) != 0:
                if product["nome_da_empresa"] not in enterprises_list:
                    enterprises_list[product["nome_da_empresa"]] = 0
                enterprises_list[product["nome_da_empresa"]] += 1
        return enterprises_list

    @classmethod
    def generate(cls, list):
        simple_report = SimpleReport.generate(list)
        enteprises_list = (
            cls.create_list_of_enteprises_and_quantity_of_their_products(list)
        )
        string = ''
        for enterprise in enteprises_list:
            string += f"- {enterprise}: {enteprises_list[enterprise]}\n"
        complete_report = (
            f"{simple_report}\nProdutos estocados por empresa: \n{string}"
        )
        return complete_report
