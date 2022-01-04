# https://www.hashtagtreinamentos.com/como-trabalhar-com-arquivos-csv-no-python?gclid=Cj0KCQiA5OuNBhCRARIsACgaiqXIP6Kj1pXLiLT5BSkDQKmPxlAndhWV_Uksba5hWdw3uhdazARVqQYaAimrEALw_wcB
# https://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith
# https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
import csv
import json

import pandas as pd

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith(".csv"):
            with open(path, mode="r") as csv_file:
                reader = csv.DictReader(csv_file)
                data = [row for row in reader]
        elif path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
        elif path.endswith(".xml"):
            data = pd.read_xml(path).to_dict(orient="records")
        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)
