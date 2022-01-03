from datetime import datetime


class SimpleReport:

    def get_first_fabricated(dict):
        first_fabricated = ''
        for products in dict:
            if first_fabricated == '':
                first_fabricated = products['data_de_fabricacao']
            elif first_fabricated > products['data_de_fabricacao']:
                first_fabricated = products['data_de_fabricacao']
        return first_fabricated

    def get_to_expire(dict):
        current_date = datetime.now().strftime("%Y/%M/%D")
        expire = ''
        for products in dict:
            if expire == '' and products['data_de_validade'] > current_date:
                expire = products['data_de_validade']
            elif expire > products['data_de_validade']:
                if products['data_de_validade'] > current_date:
                    expire = products['data_de_validade']
        return expire

    @classmethod
    def generate(self, dict):
        fabricated = self.get_first_fabricated(dict)
        expire = self.get_to_expire(dict)

        return (
            f'Data de fabricação mais antiga: {fabricated}\n'
            f'Data de validade mais próxima: {expire}\n'
        )
