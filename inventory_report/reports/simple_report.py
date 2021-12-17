from datetime import date


class SimpleReport():

    def earliest_manufact_date(products):
        earliest_manufact_date = ''
        for product in products:
            if earliest_manufact_date == '':
                earliest_manufact_date = product['data_de_fabricacao']
            elif earliest_manufact_date > product['data_de_fabricacao']:
                earliest_manufact_date = product['data_de_fabricacao']
        return earliest_manufact_date

    def closest_expiration_date(products):
        closest_expiration_date = ''
        today = date.today()
        for product in products:
            validate_date = product['data_de_validade']
            if(today.strftime("%Y-%m-%D") > validate_date):
                continue
            elif closest_expiration_date == '':
                closest_expiration_date = validate_date
            elif closest_expiration_date > validate_date:
                closest_expiration_date = validate_date
        return closest_expiration_date

    @classmethod
    def generate(cls, list):
        earliest_manufact_date = cls.earliest_manufact_date(list)
        closest_expiration_date = cls.closest_expiration_date(list)