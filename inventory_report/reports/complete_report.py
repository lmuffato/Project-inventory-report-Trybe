from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        return cls.generate_complete_report(stock)

    def generate_complete_report(stock):
        simple_stock = CompleteReport.generate_simple_stock(stock)
        parsed_company_items = CompleteReport.parse_stock_key_value_to_un_list(
            CompleteReport.get_for_each_repeated_times(
                stock,
                "nome_da_empresa",
            ),
            "Produtos estocados por empresa: ",
        )

        return f"{simple_stock}\n{parsed_company_items}"
