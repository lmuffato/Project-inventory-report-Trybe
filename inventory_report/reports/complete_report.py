from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(products_list):
        inherit = SimpleReport.generate(products_list)
        frequency = {}
        phrase = 'Produtos estocados por empresa: \n'
        company = ''
        for product in products_list:
            if (product['nome_da_empresa'] in frequency):
                frequency[product['nome_da_empresa']] += 1
            else:
                frequency[product['nome_da_empresa']] = 1
        for key, value in frequency.items():
            company += f"- {key}: {value}\n"
        report = (
          f"{inherit}\n{phrase}{company}"
          )
        return(report)
