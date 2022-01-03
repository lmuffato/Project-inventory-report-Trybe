from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class Inventory:
    def read_csv(path):
        with open(path) as file:
            reader = csv.DictReader(file)
            result = list(reader)
        return result

    def read_json(path):
      with open(path) as file:
          reader = json.load(file)
          result = list(reader)
      return result

    def import_data(file, relatory_type):
        path = file.split('.')
        extension = path[-1]
        if (extension == "csv"):
            file_read = Inventory.read_csv(file)
        if (extension == "json"):
            file_read = Inventory.read_json(file)



        if relatory_type == "simples":
            return SimpleReport.generate(file_read)
        elif relatory_type == "completo":
            return CompleteReport.generate(file_read)
        else:
            raise ValueError("Relatório inválido")
