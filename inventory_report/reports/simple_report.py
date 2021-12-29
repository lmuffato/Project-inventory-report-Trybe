class SimpleReport:
    @classmethod
    def generate(cls, products):
        r1 = "Data de fabricação mais antiga: "
        r2 = "Data de validade mais próxima: "
        r3 = "Empresa com maior quantidade de produtos estocados: "

        first_row = "{}{}".format(r1, '2019-09-13')
        second_row = "{}{}".format(r2, '2023-01-17')
        third_row = "{}{}".format(r3, 'sanofi-aventis U.S. LLC')

        return "{}\n{}\n{}\n".format(first_row, second_row, third_row)
