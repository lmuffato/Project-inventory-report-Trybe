from typing import List
from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data: List):
        today = datetime.now().strftime("%Y/%M/%D")

        def nonExpired(date):
            if date > today:
                return True
            return False

        def getProp(name):
            def curried(obj):
                return obj[name]
            return curried

        return (
            f"""Data de fabricação mais antiga: {
                min(map(getProp('data_de_fabricacao'), data))}\n"""
            f"""Data de validade mais próxima: {
                min(filter(nonExpired,
                map(getProp('data_de_validade'), data)))}\n"""
            f"Empresa com maior quantidade de produtos estocados: "
            f"""{Counter(map(
                getProp('nome_da_empresa'), data)).most_common(1)[0][0]}\n"""
        )
