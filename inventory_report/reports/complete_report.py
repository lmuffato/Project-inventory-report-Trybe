from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(list):
        baseStr = SimpleReport.generate(list)
        baseStr += "\nProdutos estocados por empresa: \n"
        cpDict = SimpleReport.countProducts(list)[1]
        for key in cpDict:
            baseStr += "- " + key + ": " + str(cpDict[key]) + "\n"
        return baseStr
