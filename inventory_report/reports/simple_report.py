from datetime import datetime


class SimpleReport:
    def generate(products_list):
        fabrication = []
        due_date = []
        frequency = {}
        now = datetime.today().strftime('%Y-%m-%d')
        for product in products_list:
            fabrication.append(product['data_de_fabricacao'])
            if product['data_de_validade'] >= now:
                due_date.append(product['data_de_validade'])
            else:
                frequency
            if (product['nome_da_empresa'] in frequency):
                frequency[product['nome_da_empresa']] += 1
            else:
                frequency[product['nome_da_empresa']] = 1
        oldest_fabrication = min(fabrication)
        newest_due_date = min(due_date)
        frequent = max(frequency)
        report = (
          f"Data de fabricação mais antiga: {oldest_fabrication}\n"
          f"Data de validade mais próxima: {newest_due_date}\n"
          f"Empresa com maior quantidade de produtos estocados: {frequent}\n")
        return(report)
