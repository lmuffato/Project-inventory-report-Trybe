
class SimpleReport():

    def earliest_manufact_date(products):
        earliest_manufact_date = ''
        for product in products:
            if earliest_manufact_date == '':
                earliest_manufact_date = product['data_de_fabricacao']
            elif earliest_manufact_date > product['data_de_fabricacao']:
                earliest_manufact_date = product['data_de_fabricacao']
        return earliest_manufact_date

    @classmethod
    def generate(cls, list):
        earliest_manufact_date = cls.earliest_manufact_date(list)
