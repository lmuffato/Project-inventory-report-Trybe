from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def complement_report(company_dict):
        complementary_report = '\nProdutos estocados por empresa: \n'
        for product in company_dict:
            complementary_report += f'- {product}: {company_dict[product]}\n'
        return (complementary_report)

    def count_products(list):
        company_list = []
        company_dict = {}
        for data in list:
            company_list.append(data["nome_da_empresa"])
        for company in company_list:
            sum = 0
            for data in list:
                if (data["nome_da_empresa"] == company):
                    sum += 1
            company_dict.update({company: sum})
        return (company_dict)

    @classmethod
    def generate(self, list):
        company_dict = self.count_products(list)
        report = SimpleReport.generate(list)
        complementary_report = self.complement_report(company_dict)
        return (report + complementary_report)
