# import inventory_report.importer.json_importer as imp
from datetime import datetime


class SimpleReport:

    @staticmethod
    def greatest_company_stock(products):
        out = dict()
        for x in products:
            try:
                out[x['nome_da_empresa']] += 1
            except KeyError:
                out[x['nome_da_empresa']] = 1
        company = max(out, key=lambda x: out[x])
        return {
            "name": company,
            "value": out[company]
        }

    @staticmethod
    def nextest_validity_date(products):
        dates = [
            converted_datetime
            for converted_datetime in [
                datetime.strptime(product['data_de_validade'], "%Y-%m-%d")
                for product in products
            ]
            if converted_datetime > datetime.now()
        ]
        return str(min(dates).date())

    @staticmethod
    def oldest_manufacture_date(products):
        dates = list(
          map(
            lambda x: datetime.strptime(x['data_de_fabricacao'], "%Y-%m-%d"),
            products
          )
        )
        return str(min(dates).date())

    @staticmethod
    def generate(products):
        great_stock = SimpleReport.greatest_company_stock(products)
        oldest_manufacture = SimpleReport.oldest_manufacture_date(products)
        latest_validity = SimpleReport.nextest_validity_date(products)

        strs = [
            f'Data de fabricação mais antiga: {oldest_manufacture}',
            f'Data de validade mais próxima: {latest_validity}',
            (
                'Empresa com maior quantidade de produtos estocados:'
                ' '
                f'{great_stock["name"]}'
            )
        ]
        out = '\n'.join(strs) + '\n'
        return out


# import pprint
# impo = imp.JsonImporter()
# json = impo.readFile('inventory_report/data/inventory.json')
# # pprint.pprint(json)
# # pprint.pprint(SimpleReport.greatest_company_stock(json))

# pprint.pprint(SimpleReport.generate(json))
