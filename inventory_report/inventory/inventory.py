import csv
from inventory_report.reports import simple_report, complete_report


class Inventory():
    def import_data(file, type):
        typeDict = {
            "simples": simple_report.SimpleReport.generate,
            "completo": complete_report.CompleteReport.generate,
        }
        dictList = []
        with open(file, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                dictList.append(row)
        return typeDict[type](dictList)
