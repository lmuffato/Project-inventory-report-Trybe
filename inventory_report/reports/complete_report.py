from _typeshed import Self
from simple_report import simple_report


class completeReport:
    def get_all_companies(list):
        company_list = set()
        for data in list:
            company_list.add(data["nome_da_empresa"])

        return company_list

    def get_quantity_of_products_by_company(list):
        company_list = Self.get_all_companies(list)
        company_dict = {}

        for company in company_list:
            sum = 0
            for data in list:
                if (data["nome_da_empresa"] == company):
                    sum += 1
            company_dict.update({company: sum})
        return company_dict

    def generate():
        simple_report.generate(list)
        company_dict = Self.get_quantity_of_products_by_company(list)
        print("produstos estocados por empresas:")
        print(company_dict)
