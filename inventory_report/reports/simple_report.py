from inventory_report.reports.filter_report_values import FilterValues


class SimpleReport:

    def generate(product_list):
        data_fabricacao = FilterValues.get_data_fabricacao(product_list)
        data_validade = FilterValues.get_data_validade(product_list)
        empresa = FilterValues.get_empresa(product_list)
        return (
            f"Data de fabricação mais antiga: {data_fabricacao}\n"
            f"Data de validade mais próxima: {data_validade}\n"
            f"Empresa com maior quantidade de produtos estocados: {empresa}\n")
