from inventory_report.reports.return_data import return_data
from collections import Counter


class SimpleReport:
    def generate(list):
        older = return_data.older_data(list)
        newer = return_data.newer_data(list)
        c = Counter(company["nome_da_empresa"] for company in list)
        company = c.most_common(1)[0][0]
        return (
            f"Data de fabricação mais antiga: {older}\n"
            f"Data de validade mais próxima: {newer}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}"
        )
