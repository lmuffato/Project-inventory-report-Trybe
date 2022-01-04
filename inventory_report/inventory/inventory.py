# https://www.hashtagtreinamentos.com/como-trabalhar-com-arquivos-csv-no-python?gclid=Cj0KCQiA5OuNBhCRARIsACgaiqXIP6Kj1pXLiLT5BSkDQKmPxlAndhWV_Uksba5hWdw3uhdazARVqQYaAimrEALw_wcB
# https://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith
# https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
import csv

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith(".csv"):
            with open(path, mode="r") as csv_file:
                reader = csv.DictReader(csv_file)
                data = [row for row in reader]
            if type == "simples":
                return SimpleReport.generate(data)
            if type == "completo":
                return CompleteReport.generate(data)
