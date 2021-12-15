# https://medium.com/data-hackers/escrita-e-leitura-de-arquivos-csv-em-python-6a256c608818
import csv
from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.simple_report import CompleteReport


class Inventory:
    def import_data(path, type):
        if (type == "simples"):
            with open(path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                csv_reader.__next__()

                SimpleReport.generate

                # for row in csv_reader:
                #     print(row[0] + ', ' + row[1] + ', ' + row[2])
