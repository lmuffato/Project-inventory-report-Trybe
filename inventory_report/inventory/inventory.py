import csv
import json
from inventory_report.reports import simple_report, complete_report


class Inventory():
    typeDict = {
            "simples": simple_report.SimpleReport.generate,
            "completo": complete_report.CompleteReport.generate,
        }

    def csvReader(file, type):
        dictList = []
        with open(file, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                dictList.append(row)
        return Inventory.typeDict[type](dictList)

    def jsonReader(file, type):
        with open(file, 'r') as jsonFile:
            data = json.load(jsonFile)
            return Inventory.typeDict[type](data)

    def import_data(file, type):
        if file.endswith("csv"):
            return Inventory.csvReader(file, type)
        elif file.endswith("json"):
            return Inventory.jsonReader(file, type)
