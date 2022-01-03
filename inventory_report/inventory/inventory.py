from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    def read_csv(path):
        with open(path, "read") as file:
            reader = csv.DictReader(file)
            result = list(reader)
        return result

    def import_data(self, file, relatory_type):
        csv_file = self.read_csv(file)
        if relatory_type == "simples":
            return SimpleReport.import_data(csv_file)
        elif relatory_type == "complete":
            return CompleteReport.import_data(csv_file)
        else:
            raise ValueError("Relatório inválido")
