from inventory_report.reports.report import ReportUtils


class SimpleReport(ReportUtils):
    @classmethod
    def generate(cls, stock):
        return cls.generate_simple_stock(stock)

    def generate_simple_stock(stock):
        oldest_date_fabrication = min(
            SimpleReport.parse_stock(stock, "data_de_fabricacao", isDate=True)
        )
        closest_date_validation = SimpleReport.get_stock_by_current_date(
            stock, "data_de_validade"
        )
        company_most_inventory = SimpleReport.get_most_repeated(
            stock, "nome_da_empresa"
        )

        return f"""Data de fabricação mais antiga: {oldest_date_fabrication}
Data de validade mais próxima: {closest_date_validation}
Empresa com maior quantidade de produtos estocados: {company_most_inventory}
"""
