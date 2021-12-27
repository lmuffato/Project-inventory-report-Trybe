import csv
from inventory_report.reports.simple_report import SimpleReport

# from inventory_report.reports.complete_report import


class Inventory:
    def import_data(path, type):
        if path.endswith(".csv"):
            with open(path, mode="r") as files:
                file = csv.DictReader(files)
                data = [row for row in file]
        if type == "simples":
            return SimpleReport.generate(data)
        # if type == "completo":
        #   return  CompleteReport.generate(data)


Inventory.import_data("inventory_report/data/inventory.csv", "simples")
