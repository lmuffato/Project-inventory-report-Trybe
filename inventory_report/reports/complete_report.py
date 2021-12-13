from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__():
        pass

    def generate(dic_arr):
        first_half = SimpleReport.generate(dic_arr)
        company_arr = []
        for dic in dic_arr:
            company_arr.append(dic["nome_da_empresa"])
        seccond_half = "Produtos estocados por empresa: \n"
        controll_arr = []
        for company in company_arr:
            if (company not in controll_arr):
                controll_arr.append(company)
                qtt = company_arr.count(company)
                seccond_half += f"- {company}: {qtt}\n"
        return (f"{first_half}\n"
                f"{seccond_half}")
