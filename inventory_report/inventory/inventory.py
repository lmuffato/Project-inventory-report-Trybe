from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    def read_csv(path):
        with open(path) as file:
            reader = csv.DictReader(file)
            result = list(reader)
        return result

    def import_data(file, relatory_type):
        csv_file = Inventory.read_csv(file)
        if relatory_type == "simples":
            return SimpleReport.generate(csv_file)
        elif relatory_type == "completo":
            return CompleteReport.generate(csv_file)
        else:
            raise ValueError("Relatório inválido")
