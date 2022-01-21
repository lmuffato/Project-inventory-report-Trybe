import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        list = []
        with open(path) as file:
            products_csv = csv.DictReader(file)
            for product in products_csv:
                list.append(product)

        if type == "simples":
            return SimpleReport.generate(list)
        if type == "completo":
            return CompleteReport.generate(list)
