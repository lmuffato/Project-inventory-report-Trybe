from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv


class Inventory:
    def import_data(path, type):
        data = []
        with open(path) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                data.append(rows)

        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)


Inventory.import_data('inventory_report/data/inventory.csv', 'simples')
