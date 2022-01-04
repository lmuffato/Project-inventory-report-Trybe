from datetime import datetime
from collections import Counter


class SimpleReport:
    def oldest_manufacturing_date(today, path, older):
        item = iter(path)
        while item:
            try:
                result = next(item)
                if older > result["data_de_fabricacao"]:
                    older = result["data_de_fabricacao"]
            except StopIteration:
                break
        return older

    def nearest_expiration_date(today, path, validate):
        item = iter(path)
        while item:
            try:
                result = next(item)
                element = result["data_de_validade"]
                if (validate > element) and today < element:
                    validate = result["data_de_validade"]
            except StopIteration:
                break
        return validate

    def count_products(list):
        lista = []
        item = iter(list)
        while item:
            try:
                result = next(item)
                lista.append(result["nome_da_empresa"])
            except StopIteration:
                break
        __quantidades = Counter(lista)
        return __quantidades

    @classmethod
    def generate(self, path):
        today = datetime.today().strftime("%Y-%m-%d")
        date_reference = "3000-01-01"
        date_older = self.oldest_manufacturing_date(
            today, path, date_reference
        )
        nearest_validity = self.nearest_expiration_date(
            today, path, date_reference
        )
        nome = self.count_products(path).most_common()[0][0]
        return (
            f"Data de fabricação mais antiga: {date_older}\n"
            f"Data de validade mais próxima: {nearest_validity}\n"
            f"Empresa com maior quantidade de produtos estocados: {nome}\n"
        )
