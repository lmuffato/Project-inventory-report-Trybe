from datetime import date


class SimpleReport:
    def get_oldest_date(dictData):
        dates = []
        for value in dictData:
            dates.append(date.fromisoformat(value["data_de_fabricacao"]))
        return min(dates)

    def get_closest_date(dictData):
        dates = []
        for value in dictData:
            valueDate = date.fromisoformat(value["data_de_validade"])
            currentDate = date.today()
            if (valueDate > currentDate):
                dates.append(valueDate)
        return min(dates)

    def get_company_with_more_stocked_products(dictData):
        names = []
        for value in dictData:
            names.append(value["nome_da_empresa"])
        return max(names, key=names.count)

    @classmethod
    def generate(cls, dictData):
        oldest_fabrication_date = cls.get_oldest_date(dictData)
        closest_valid_date = cls.get_closest_date(dictData)
        company_with_more_stocked_products = (
            cls.get_company_with_more_stocked_products(dictData)
        )

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {closest_valid_date}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {company_with_more_stocked_products}\n"
        )
