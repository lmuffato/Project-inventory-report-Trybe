from csv import DictReader
from functools import lru_cache


from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    """
    Implementação baseada no projeto anterior Job Insights
    """
    @lru_cache
    def import_data(path):
        if path.endswith(".csv"):
            with open(path) as file:
                data = list(DictReader(file))
                return data
        raise ValueError("Arquivo inválido")
