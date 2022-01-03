from collections import defaultdict
from datetime import datetime


def dates(list):
    manifacturingList = map(lambda dict: dict["data_de_fabricacao"], list)
    validation = map(lambda dict: dict["data_de_validade"], list)
    now = datetime.today()

    def filtering(date):
        return datetime.strptime(date, '%Y-%m-%d') > now
    filteredValidation = filter(filtering, validation)
    return {
        'fabrication': min(manifacturingList),
        'validation': min(filteredValidation),
    }


def countProducts(list):
    generalDict = defaultdict(int)
    for dict in list:
        generalDict[dict["nome_da_empresa"]] += 1
    comparisonValue = 0
    company = ''
    for key in generalDict:
        if generalDict[key] > comparisonValue:
            comparisonValue = generalDict[key]
            company = key
    return company


class SimpleReport():
    def generate(list):
        datesDict = dates(list)
        company = countProducts(list)
        returnStr = ''
        returnDict = {
            "Data de fabricação mais antiga": datesDict["fabrication"],
            "Data de validade mais próxima": datesDict["validation"],
            "Empresa com maior quantidade de produtos estocados": company,
        }
        for key in returnDict:
            returnStr += key + ': ' + returnDict[key] + '\n'
        return str(returnStr)
