from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import pandas as pd


class Inventory:
    def readFile(path):
        if path.endswith(".csv"):
            file = pd.read_csv(path).to_dict(orient="records")

        return file

    @classmethod
    def import_data(cls, path, type):
        file = cls.readFile(path)

        if type == "simples":
            report = SimpleReport.generate(file)
        if type == "completo":
            report = CompleteReport.generate(file)
        return report
