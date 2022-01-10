import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    r_func = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    def import_data(file_path, report_type):
        cont = list()

        if file_path.endswith(".csv"):
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                cont = [row for row in reader]

        elif file_path.endswith(".json"):
            with open(file_path, "r") as file:
                cont = json.load(file)

        else:
            raise ValueError("Arquivo inválido")
        return Inventory.r_func[report_type](cont)
