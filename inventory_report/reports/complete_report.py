from inventory_report.reports.simple_report import (
    SimpleReport,
    FunctionsReport,
)


class StockProducts():
    @classmethod
    def companies_prod(cls, list_prod):
        all_comp = FunctionsReport.companies(list_prod)
        comps = '\n'.join(f'- {comp}: {val}' for comp, val in all_comp.items())
        return (
            f'Produtos estocados por empresa: \n'
            f'{comps}'
        )


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list_prod):
        simple_report = super().generate(list_prod)
        all_companies = StockProducts.companies_prod(list_prod)
        return (
            f'{simple_report}\n'
            f'{all_companies}\n'
<<<<<<< HEAD
        )
=======
        )
>>>>>>> paulovitorInventoryReport
