from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def serialize(list):
        count_product_manufacturing = ""
        for item in list:
            count_product_manufacturing += f"- {item}: {list[item]}\n"
        return count_product_manufacturing

    @classmethod
    def generate(self, path):

        products_stocked_report = self.serialize(
            SimpleReport.count_products(path)
        )

        return (
            f"{SimpleReport.generate(path)}\n"
            f"Produtos estocados por empresa: \n"
            f"{products_stocked_report}"
        )
